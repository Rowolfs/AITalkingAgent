import whisper as whisper_runner

model = whisper_runner.load_model("base")


def transcribe(path: str):
    audio = whisper_runner.load_audio(path)
    audio = whisper_runner.pad_or_trim(audio)

    mel = whisper_runner.log_mel_spectrogram(audio, n_mels=model.dims.n_mels).to(model.device)
    _, probs = model.detect_language(mel)
    print(f"Detected language: {max(probs, key=probs.get)}")

    options = whisper_runner.DecodingOptions()
    result = whisper_runner.decode(model, mel, options)
    print(result.text)
    return result.text
    
