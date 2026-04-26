from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

def summarize_txt(file_path: str):
    client = OpenAI(api_key = api_key)

    with open(file_path, 'r', encoding = 'utf-8') as f:
        txt = f.read()

    system_prompt = f'''
    너는 다음 글을 요약하는 봇이다. 아래 글을 읽고, 주요 내용을 요약하라.

    작성해야 하는 포맷은 다음과 같다.

    # 대상자 정보

    ## 주요 내용

    ## 위험 요소

    ## 향후 필요한 대처

    ========== 이하 텍스트 ==========

    { txt }
    '''

    print(system_prompt)
    print('================================================')

    response = client.chat.completions.create(
        model = "gpt-4o",
        temperature = 0.1,
        messages = [
            {"role": "system", "content": system_prompt},
        ]
    )

    return response.choices[0].message.content

if __name__ == '__main__':
    file_path = 'output/20260418_with_preprocessing.txt'

    summary = summarize_txt(file_path)
    print(summary)

    with open('output/crop_model_summary.txt', 'w', encoding = 'utf-8') as f:
        f.write(summary)