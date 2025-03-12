import string

text = input("Введіть свій текст:")

for char in string.punctuation + "":
    text = text.replace(char, "")
words = text.split()

text_rules = "".join(word.capitalize() for word in words)

if len(text_rules) > 140:
    text_rules = text_rules[:140]

text_rules = "#" + text_rules

print(text_rules)