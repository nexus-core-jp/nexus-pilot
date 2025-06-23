# Nexus-Pilot

**Nexus-Pilot** is an experimental prompt-layered conversational agent designed to explore structured proposal generation and evaluation in large language models (LLMs). It uses a multi-stage prompt chaining strategy to simulate deliberation, rather than relying on fine-tuned behavior.

## Key Features

- **Multi-stage prompting**:
  - Step 1: Understand the user's intent
  - Step 2: Generate diverse response candidates
  - Step 3: Meta-evaluate and select a preferred option
- **OpenAI Chat API-compatible**
- **Runs on a private LLM backend** (parameter scale: 100B+)

> Note: This system does not disclose model weights or architectural details due to research constraints.

## Deployment

```bash
docker build -t nexus-pilot .
docker run -p 8000:8000 nexus-pilot

API Usage
Follows the OpenAI ChatCompletion format:

POST /v1/chat/completions

Accepts:

model: string

messages: list of role/content pairs

temperature: float (optional)

{
  "model": "nexus-pilot",
  "messages": [
    {"role": "user", "content": "アイデアを3案出して"}
  ],
  "temperature": 0.7
}


---

## Setup

1. Ensure you have **Python 3.9+** installed.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set required environment variables:
   - `OPENAI_API_KEY` - token for the model backend

## Running the API

Start the service with Uvicorn:
```bash
uvicorn api:app --host 0.0.0.0 --port 8000
```
The endpoint will be available at `http://localhost:8000/v1/chat/completions`.

## Usage Example

Call the API with **curl**:
```bash
curl -X POST http://localhost:8000/v1/chat/completions \
     -H "Content-Type: application/json" \
     -d '{"model": "nexus-pilot", "messages": [{"role": "user", "content": "Hello"}]}'
```

Or from Python:
```python
import requests

payload = {
    "model": "nexus-pilot",
    "messages": [{"role": "user", "content": "Hello"}]
}
resp = requests.post("http://localhost:8000/v1/chat/completions", json=payload)
print(resp.json())
```

