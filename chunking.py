# splitting the text and chunking 

import nltk
from nltk.tokenize import sent_tokenize

# run below line for the first time as it require the package below
nltk.download('punkt')

def chunk_text(page_text: str, max_words: int = 300):
    """
    Splits page text into smaller chunks based on sentences,
    ensuring each chunk is at most `max_words` long.
    :param page_text: The full text of one page.
    :param max_words: Maximum number of words per chunk.
    :return: List of text chunks.
    """
    sentences = sent_tokenize(page_text)
    chunks = []
    current_chunk = []
    word_count = 0

    for sentence in sentences:
        count = len(sentence.split())
        if word_count + count > max_words:
            chunks.append(" ".join(current_chunk))
            current_chunk, word_count = [], 0
        current_chunk.append(sentence)
        word_count += count

    if current_chunk:
        chunks.append(" ".join(current_chunk))
    return chunks