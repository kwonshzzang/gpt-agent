from pyexpat.errors import messages

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("AI_PLATFORM_API_KEY")

client = OpenAI(api_key=api_key)

messages = [
    {"role":"system", "content":"너는 사용자를 도와주는 상담사야."},
]

def get_ai_response(messages):
    response = client.chat.completions.create(
        model="gpt-4o",     # 응답 생성에 사용할 모델 지정
        temperature=0.9,    # 응답 생성에 사용할 temperature 설정
        messages=messages,  # 대화 기록을 입력으로 전달
    )

    return response.choices[0].message.content

while True:
    user_input = input("사용자: ")  # 사용자 입력받기

    if user_input == "exit":
        break

    messages.append({"role":"user", "content": user_input})
    ai_response = get_ai_response(messages) # 대화 기록을 기반으로 AI 응답 가져오기
    messages.append({"role":"assistant", "content": ai_response})
    print("AI: " + ai_response) # AI 응답 출력