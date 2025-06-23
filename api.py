from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    model: str
    messages: List[Message]
    temperature: float = 1.0

class ChatChoice(BaseModel):
    message: Message

class ChatResponse(BaseModel):
    choices: List[ChatChoice]

@app.post("/v1/chat/completions", response_model=ChatResponse)
def chat_completions(req: ChatRequest) -> ChatResponse:
    reply = Message(role="assistant", content="This is a placeholder response.")
    return ChatResponse(choices=[ChatChoice(message=reply)])
