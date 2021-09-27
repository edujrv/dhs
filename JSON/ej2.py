'''2. Agregar al programa anterior el camino inverso'''

import json


file  = open ("JSON//almacen.json","r")

nombre = None
apellido = None
edad = None
ingredientes = list()
altura = None
can_lapices = dict()
vivo = None

data = json.load(file)

nombre = data["Nombre"]
apellido = data["Apellido"]
edad = data["Edad"]
ingredientes = data["Ingredientes"]
altura = data["Altura"]
can_lapices = data["Cant-Lapices"]
vivo = data["Vivo?"]

print("Nombre: "+str(nombre)+"\n"+str(type(nombre)))
print("Apellido: "+str(apellido)+"\n"+str(type(apellido)))
print("Edad: "+str(edad)+"\n"+str(type(edad)))
print("Ingredientes: "+str(ingredientes)+"\n"+str(type(ingredientes)))
print("Altura: "+str(altura)+"\n"+str(type(altura)))
print("Cantida_Lapices: "+str(can_lapices)+"\n"+str(type(can_lapices)))
print("Vivo?: "+str(vivo)+"\n"+str(type(vivo)))