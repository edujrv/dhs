'''4. Escribir un programa en Python que permita leer información de un tres
json, las combine y lo almacene en toda en un cuarto archivo'''

import json

agrupador = dict()

file  = open ("JSON//primer.json","r")
data = json.load(file)
agrupador.update({"Nombre":data["Nombre"]})
file.close()
##
file  = open ("JSON//segundo.json","r")
data = json.load(file)
agrupador.update({"Apellido":data["Apellido"]})
file.close()
##
file  = open ("JSON//tercer.json","r")
data = json.load(file)
agrupador.update({"Edad":data["Edad"]})
file.close()
##
file  = open ("JSON//cuarto.json","w")

jsonstr = json.dumps(agrupador)
file2 = open("JSON//cuarto.json","w")
file2.write(jsonstr)
file2.close()