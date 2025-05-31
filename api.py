from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional, Dict

app = FastAPI(title="Nexus-Pilot")


class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    model: str
    messages: List[Message]
    temperature: Optional[float] = 0.7


class ChatResponse(BaseModel):
    id: str
    object: str = "chat.completion"
    choices: List[Dict]
    usage: Dict = {}


def simple_chain(messages: List[Message]) -> str:
    """Placeholder chaining logic that returns a static response."""
    if messages:
        return f"Received {len(messages)} message(s). This is a placeholder response."
    return "No messages provided."


@app.post("/v1/chat/completions", response_model=ChatResponse)
def create_chat_completion(req: ChatRequest) -> ChatResponse:
    content = simple_chain(req.messages)
    choice = {
        "index": 0,
        "message": {"role": "assistant", "content": content},
        "finish_reason": "stop",
    }
    return ChatResponse(id="dummy", choices=[choice])


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
