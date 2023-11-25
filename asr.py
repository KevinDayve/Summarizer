import whisper
def transcribe(path):
    model = whisper.load_model("base")
    results = model.transcribe(path)
    text = results["text"]
    return text