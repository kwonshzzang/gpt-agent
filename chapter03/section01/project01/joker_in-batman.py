from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY") # 환경 변수에서 API키 가져오기
client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model="gpt-4o",
    temperature=0.9,
    messages=[
        {"role":"system", "content":"너는 배트맨에 나오는 조커야. 조커의 악당 캐릭터에 맞게 답변해 줘."},
        {"role":"user", "content":"세상에서 누가 제일 아름답니?"}
    ]
)

print(response.choices[0].message.content)