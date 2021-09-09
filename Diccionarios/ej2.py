# Agregar la key cuarenta y su respectivo valor al ejercicio
#  del apartado an-terior

keys = ['Diez', 'Veinte', 'Treinta']
values = [10, 20, 30]

diccionario = dict()

for i in range(3):
    diccionario[keys[i]] = values[i]

diccionario["Cuarenta"] = 40

print("El diccionario es: ", diccionario)