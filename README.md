# AITalkingAgent

> Telegram bot for voice-to-voice conversations with a local LLM — no external AI APIs, runs fully on your own server.

```
🎙 Voice message → Whisper (STT) → Ollama (LLM) → Piper TTS → 🔊 Voice reply
```

## Features

- 🎙 **Voice input** — send a voice message, get a voice reply
- 🧠 **Local LLM** — any Ollama-compatible model (llama3, mistral, gemma3…)
- 🔊 **Text-to-speech** — natural voice synthesis via Piper TTS
- 📝 **Speech-to-text** — transcription via OpenAI Whisper (runs locally)
- 🐳 **Fully containerized** — one `docker compose up`, no local Python setup needed

## Stack

| Component        | Technology              |
|------------------|-------------------------|
| Bot framework    | Python, aiogram         |
| Speech-to-Text   | OpenAI Whisper (local)  |
| LLM inference    | Ollama                  |
| Text-to-Speech   | Piper TTS               |
| Runtime          | Docker Compose          |

## Quick Start

**1. Clone the repo**
```bash
git clone https://github.com/Rowolfs/AITalkingAgent.git
cd AITalkingAgent
```

**2. Create `.env` in the project root**
```env
TOKEN=your_telegram_bot_token
```

**3. Run**
```bash
docker compose up --build
```

Open your bot in Telegram, send a voice message — it will reply with a generated voice.

## Requirements

- Docker & Docker Compose
- Telegram Bot Token ([get one from @BotFather](https://t.me/BotFather))
- ~4 GB RAM for the default model

## How It Works

```
User sends voice message
        │
        ▼
   Bot receives .ogg file
        │
        ▼
   Whisper transcribes audio → text
        │
        ▼
   Text sent to Ollama (local LLM)
        │
        ▼
   LLM generates text response
        │
        ▼
   Piper TTS synthesizes audio
        │
        ▼
   Bot sends voice reply to user
```

## Changing the LLM Model

Pull any model via Ollama and update the bot config:

```bash
ollama pull mistral
ollama pull gemma3
ollama pull llama3
```

## Project Structure

```
AITalkingAgent/
├── bot/                  # Bot source code
├── docker-compose.yaml   # Service definitions
├── .gitignore
└── README.md
```

## License

MIT
