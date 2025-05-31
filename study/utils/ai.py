import openai

def generate_question_from_topic(topic):
    prompt = f"Buat satu soal pilihan ganda beserta jawabannya untuk topik: {topic}."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']
