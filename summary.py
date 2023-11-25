from transformers import pipeline

def summarise_text(text, max_length = 130, min_length = 30):
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length = max_length, min_length = min_length, do_sample = False)
    return summary[0]["summary_text"]
