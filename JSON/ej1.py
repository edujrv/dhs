'''1. Escribir un programa en Python que permita convertir tipos de datos de
Python a JSON'''

import json


file  = open ("JSON//almacen.json","r")

nombre = "Alejandro"
apellido = "UlaUla"
edad = 365
ingredientes = ["zanahorias", "lechuga", "tomate", "guacamole"]
altura = 185.6
can_lapices = {"Rojos" : 5, "Azules" : 2, "Verdes" : 1, "Amarillos" : 66}
vivo = True

data = json.load(file)

if data["Nombre"] == nombre:
    data["Nombre"] = None
else:
    data["Nombre"] = nombre
###
if data["Apellido"] == apellido:
    data["Apellido"] = None
else:
    data["Apellido"] = apellido
###
if data["Edad"] == edad:
    data["Edad"] = None
else:
    data["Edad"] = edad
###
if data["Ingredientes"] == ingredientes:
    data["Ingredientes"] = None
else:
    data["Ingredientes"] = ingredientes
###
if data["Altura"] == altura:
    data["Altura"] = None
else:
    data["Altura"] = altura
###
if data["Cant-Lapices"] == can_lapices:
    data["Cant-Lapices"] = None
else:
    data["Cant-Lapices"] = can_lapices
###
if data["Vivo?"] == vivo:
    data["Vivo?"] = None
else:
    data["Vivo?"] = vivo

jsonstr = json.dumps(data)
file2 = open("JSON//almacen.json","w")
file2.write(jsonstr)
file2.close()