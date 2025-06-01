# study/ai_utils.py
import openai

openai.api_key = 'API_KEY_MU'  # ganti dengan API key asli

def generate_question(topic):
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=f"Buatkan satu pertanyaan pilihan ganda tentang topik: {topic}. Sertakan jawabannya. Format: Pertanyaan - Jawaban",
        max_tokens=100
    )
    text = response.choices[0].text.strip()

    if "Jawaban:" in text:
        parts = text.split("Jawaban:")
        question = parts[0].replace("Pertanyaan:", "").strip()
        answer = parts[1].strip()
    else:
        question = text
        answer = "Tidak ditemukan"

    return question, answer