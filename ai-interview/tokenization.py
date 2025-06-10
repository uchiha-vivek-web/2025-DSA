# tokenizers.py

import nltk
import spacy
from transformers import AutoTokenizer

# One-time downloads
nltk.download('punkt', quiet=True)
nlp = spacy.load("en_core_web_sm")


def simple_whitespace_tokenizer(text: str):
    return text.split()


def nltk_word_tokenizer(text: str):
    from nltk.tokenize import word_tokenize
    return word_tokenize(text)


def nltk_sentence_tokenizer(text: str):
    from nltk.tokenize import sent_tokenize
    return sent_tokenize(text)


def spacy_tokenizer(text: str):
    doc = nlp(text)
    return [token.text for token in doc]


def huggingface_tokenizer(text: str, model_name: str = "bert-base-uncased"):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    tokens = tokenizer.tokenize(text)
    token_ids = tokenizer.convert_tokens_to_ids(tokens)
    return {"tokens": tokens, "token_ids": token_ids}
