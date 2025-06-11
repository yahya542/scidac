import requests
import json
from rapidfuzz import fuzz

def ai_response(topic):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": "Bearer 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",  # Ganti dengan API key kamu
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:8000",  
        "X-Title": "SCIDAC",  
    }
    data = {
        "model": "deepseek/deepseek-r1-0528-qwen3-8b:free",
        "messages": [
            {
                "role": "user",
                "content": f"Buatkan satu pertanyaan dan jawaban tentang topik: {topic} tapi pertanyaannya tingkat mudah saja jangan yang sulit. Format jawabanmu harus seperti:\nPertanyaan: ...\nJawaban: ..."

            }
        ]
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    response.raise_for_status()

    result = response.json()
    message = result["choices"][0]["message"]["content"]

    
    lines = message.split("\n")
    question = ""
    answer = ""

    for line in lines:
        if "Pertanyaan:" in line:
            question = line.replace("Pertanyaan:", "").strip()
        elif "Jawaban:" in line:
            answer = line.replace("Jawaban:", "").strip()

   
    if not question or not answer:
        question, answer = message.strip().split("?")
        question += "?"
        answer = answer.strip()

    return question, answer



def check_answer(user_answer, correct_answer, question):
    # Normalisasi dulu, misal lowercase dan strip spasi
    ua = user_answer.lower().strip()
    ca = correct_answer.lower().strip()
    
    # Cek similarity dengan rapidfuzz, threshold misal 70
    similarity = fuzz.ratio(ua, ca)
    if similarity >= 70:
        return True, "Jawaban kamu benar!"
    
    # Kalau similarity kurang, panggil AI untuk penilaian lebih lanjut
    import requests, json
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": "Bearer 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", 
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:8000",
        "X-Title": "SCIDAC",
    }
    prompt = f"""
    Pertanyaan: {question}
    Jawaban Pengguna: {user_answer}
    Jawaban Benar: {correct_answer}

    Apakah jawaban pengguna sudah benar? Jika benar, jawab 'benar' saja. Jika salah, jawab 'salah' dan berikan koreksi.
    """

    data = {
        "model": "deepseek/deepseek-r1-0528-qwen3-8b:free",
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    response.raise_for_status()
    result = response.json()
    message = result["choices"][0]["message"]["content"].strip().lower()

    if "benar" in message and "salah" not in message:
        return True, "Jawaban kamu benar!"
    else:
        return False, message
