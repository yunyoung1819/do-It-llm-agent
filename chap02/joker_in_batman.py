from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY") # 환경변수에서 API 키 가져오기

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model="gpt-4o",
    temperature=0.9,
    messages=[
        {"role": "system", "content": "너는 영화 다크나이트에 나오는 히스레저가 연기한 조커야. 히스레저 조커의 악당 캐릭터에 맞게 답변해줘."},
        {"role": "user", "content": "나는 나이가 많은데 연애를 못했어"},
    ]
)

print(response.choices[0].message.content)