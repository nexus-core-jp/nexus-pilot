from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel

from prompt_chainer import PromptChainer


class Message(BaseModel):
    role: str
    content: str


class ChatCompletionRequest(BaseModel):
    model: str
    messages: List[Message]
    temperature: Optional[float] = 0.7


app = FastAPI(title="Nexus-Pilot")
chainer = PromptChainer()


@app.post("/v1/chat/completions")
def create_chat_completion(payload: ChatCompletionRequest):
    # get last user message
    user_msg = ""
    for msg in reversed(payload.messages):
        if msg.role == "user":
            user_msg = msg.content
            break
    result = chainer.run(user_msg)
    return {
        "model": payload.model,
        "choices": [
            {"message": {"role": "assistant", "content": result}}
        ],
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
