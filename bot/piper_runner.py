import wave
import io
import subprocess
import sys
from piper import PiperVoice

def download_voices
subprocess.run([sys.executable, "-m", "piper.download_voices", "ru_RU-irina-medium"])
voice = PiperVoice.load("./ru_RU-irina-medium.onnx")

def gen_speech_bytes(text: str) -> io.BytesIO:
    buffer = io.BytesIO()
    with wave.open(buffer, "wb") as wav_file:
        wav_file.setnchannels(1)        # моно
        wav_file.setsampwidth(2)        # 16-bit PCM
        wav_file.setframerate(24000)
        voice.synthesize_wav(text, wav_file)
    buffer.seek(0) 
    return buffer



