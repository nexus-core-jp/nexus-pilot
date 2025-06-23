from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_chat_completions_returns_response():
    resp = client.post(
        "/v1/chat/completions",
        json={
            "model": "nexus-pilot",
            "messages": [{"role": "user", "content": "Hello"}],
            "temperature": 0.5,
        },
    )
    assert resp.status_code == 200
    data = resp.json()
    assert "choices" in data
    assert data["choices"][0]["message"]["role"] == "assistant"
