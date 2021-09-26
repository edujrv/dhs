'''
Diseñar un programa calcule la raíz cuadrada de cada elemento de unalista. Utilizar map().
'''
import math


lista = [32,5435,543,2,34,5,234,2,4326,67,856,89]

raices = list (map(math.sqrt,lista))

print(raices)