import wave
import io
import subprocess
import os
import sys
from piper import PiperVoice
from config import config
from logger import logger

voice_name = config['piper_tts']['voice']
onnx_path = f"./{voice_name}.onnx"

if not os.path.exists(onnx_path):
    logger.info(f"Начинаем загрузку модели голоса: {voice_name}")
    subprocess.run([sys.executable, "-m", "piper.download_voices", voice_name], check=True, stdout=sys.stdout,
    stderr=sys.stderr)
    if not os.path.exists(onnx_path):
        raise FileNotFoundError(f"Файл голоса не найден: {onnx_path}. Проверьте загрузку.")
    logger.info("Загрузка завершена успешно")
voice = PiperVoice.load(onnx_path)

def gen_speech_bytes(text: str) -> io.BytesIO:
    buffer = io.BytesIO()
    with wave.open(buffer, "wb") as wav_file:
        wav_file.setnchannels(config['piper_tts']['num_channels'])        # моно
        wav_file.setsampwidth(config['piper_tts']['bits_per_sample'])        # 16-bit PCM
        wav_file.setframerate(config['piper_tts']['samplerate'])
        voice.synthesize_wav(text, wav_file)
    buffer.seek(0) 
    return buffer



