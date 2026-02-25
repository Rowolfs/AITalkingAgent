### AITalkingAgent - is a Telegram bot for voice‑to‑voice chat using Whisper, Ollama and Piper TTS.
# Features

    Send voice messages and get voice replies.

    Speech‑to‑text via Whisper.

    Local LLM via Ollama.

    Text‑to‑speech via Piper TTS.

    All services run in Docker, no local setup.

# Quick Start

1. Clone the repo:
```bash
git clone https://github.com/Rowolfs/AITalkingAgent.git
cd AITalkingAgent
```
2. Create .env in the project root:
```text
TOKEN=1234567890:ABCDEF...
```
3. Run:
```bash
docker compose up --build
```
```bash
docker-compose up --build #on older Docker
```

Open your bot in Telegram, send a voice message, and it will answer you with a generated voice reply.