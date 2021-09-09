# Borrar la key "veinte" y su respectivo valor
#  al ejercicio del apartado anterio

keys = ['Diez', 'Veinte', 'Treinta']
values = [10, 20, 30]

diccionario = dict()

for i in range(3):
    diccionario[keys[i]] = values[i]

print("El diccionario es: ", diccionario)

print("Se agrega la key cuarenta y su valor")
diccionario["Cuarenta"] = 40
print("El diccionario es: ", diccionario)

print("Se borra la key veinte")
diccionario.pop("Veinte")
print("El diccionario es: ", diccionario)