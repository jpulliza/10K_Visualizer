from gensim.summarization.summarizer import summarize

def summarize_sentences(sentences):
    text = []
    for sentence in sentences:
        text = text + ". " + sentence
    return summarize(text)

