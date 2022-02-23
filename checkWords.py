import logging

from uzwords import words
from difflib import get_close_matches
import transliterate

def checkWords(word, Words=words):
    word = word.lower()
    matches = set(get_close_matches(word,Words,n=5))
    available = False

    if word in matches:
        available = True
        matches = word
    elif "х" in word:
        word=word.replace("х", "ҳ")
        matches.update(get_close_matches(word,words,n=5))
    elif "ҳ" in word:
        word = word.replace("ҳ", "х")
        matches.update(get_close_matches(word,words,n=5))

    return {"available":available, "matches":matches}