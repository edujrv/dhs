'''
Diseñar un programa calcule la raíz cuadrada de cada elemento de unalista. Utilizar map().
'''
#TODO: Como era igual al anterior, voy a calcular el cuadrado de cada elemento de una lista


lista = [2,4,56,6,4,34,2,5,6,3,6]

lista_de_cuadrados = list (map ( lambda x: x*x, lista ))

print(lista_de_cuadrados)