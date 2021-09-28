'''3. Escribir un programa en Python que permita leer información de un ar-
chivo json y mostrarla por pantalla de forma ordenada'''

'''2. Agregar al programa anterior el camino inverso'''

import json

file  = open ("JSON//almacen.json","r")

data = json.load(file)

print("Lectura: "+str(data)+"\n")
