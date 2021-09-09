# Convertir las siguientes listas a un diccionario:
# keys = [’Diez’, ’Veinte’, ’Treinta’]
# values = [10, 20, 30]

keys = ['Diez', 'Veinte', 'Treinta']
values = [10, 20, 30]

diccionario = dict()

for i in range(3):
    diccionario[keys[i]] = values[i]

print("El diccionario es: ", diccionario)