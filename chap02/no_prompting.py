from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key= os.getenv("OPENAI_API_KEY") # 환경변수에서 API 키 가져오기

client = OpenAI(api_key = api_key)