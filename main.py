from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()

class Message(BaseModel):
    question: str

@app.post("/ask")
def ask_ai(msg: Message):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": msg.question}]
    )
    answer = response.choices[0].message["content"]
    return {"answer": answer}
