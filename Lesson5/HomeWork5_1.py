import string
import keyword

sentence = input("Введіть слово:")
sentence_valid = True

if sentence and sentence[0].isdigit():
    sentence_valid = False

if any(c.isupper() for c in sentence):
    sentence_valid = False

if any (c in string.punctuation.replace("_", "") or c.isspace() for c in sentence):
    sentence_valid = False

if sentence in keyword.kwlist:
    sentence_valid = False

if sentence.count("_") > 1:
    sentence_valid = False

print(sentence_valid)
