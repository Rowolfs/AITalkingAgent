import wave
import io
from piper import PiperVoice

voice = PiperVoice.load("./voices/ru_RU-ruslan-medium.onnx")

def gen_speech_bytes(text: str) -> io.BytesIO:
    buffer = io.BytesIO()
    with wave.open(buffer, "wb") as wav_file:
        wav_file.setnchannels(1)        # моно
        wav_file.setsampwidth(2)        # 16-bit PCM
        wav_file.setframerate(24000)
        voice.synthesize_wav(text, wav_file)
    buffer.seek(0) 
    return buffer



