'''1. Escribir un programa en Python que verifique si una cadena de texto
comienza con una palabra'''
import re

text = "Los cajas son malas, nunca te va a tocar algo"
pattern = re.compile("Los")
print(pattern.match(text))