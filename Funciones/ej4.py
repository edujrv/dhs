'''
Escribir una función que reciba una lista y retorne una nueva lista con los elementos de la primera sin repeticiones
'''

def quitar_repetidos(lista):
    nuevaLista = set()
    for elemento in lista:
        nuevaLista.add(elemento)

    return nuevaLista

lista = [1,2,3,4,5,3,3,3,54,5]

listaSinRepetidos = quitar_repetidos(lista)

print(listaSinRepetidos)

