'''2. Escribir un programa en Python que a partir de un string, separe en una
lista todas las palabras que contengan una "u" y finalicen en "b".'''

import re

text = "Play game tumb tumblr gumb sound dumb numb bum bone rumb tax hound deb"
pattern = re.compile(r"\b.u.b\b")
print(pattern.findall(text))