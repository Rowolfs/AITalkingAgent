#!/usr/bin/env python
# pylint: disable=unused-argument
# This program is dedicated to the public domain under the CC0 license.



import logging
import os
import whisper_runner
import piper_runner
import ollama_runner
from config import token

from telegram import ForceReply, Update, InputFile
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import aiofiles
import subprocess


# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}! This Ai Talking Agent send audio message to bot",
        reply_markup=ForceReply(selective=True),
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")


async def talk(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка голосового сообщения."""
    voice = update.message.voice
    if not voice:
        await update.message.reply_text("Это не голосовое сообщение 😅")
        return

    file = await context.bot.get_file(voice.file_id)
    ogg_path = f"/tmp/{voice.file_id}.ogg"
    wav_path = f"/tmp/{voice.file_id}.wav"

    await file.download_to_drive(ogg_path)

    subprocess.run(
        ["ffmpeg", "-i", ogg_path, "-ar", "16000", "-ac", "1", wav_path],
        check=True,
    )

    text = whisper_runner.transcribe(wav_path)
    text = ollama_runner.ask_ollama(text)
    print(text)
    audio_buffer = piper_runner.gen_speech_bytes(text)

    await update.message.reply_voice(voice=InputFile(audio_buffer, filename="answer.wav"))

    # Чистим временные файлы
    os.remove(ogg_path)
    os.remove(wav_path)

def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    
    application = (
        ApplicationBuilder()
        .token(token)
        .connect_timeout(60)
        .read_timeout(120)
        .write_timeout(120)
        .build()
    )

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.VOICE, talk))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()