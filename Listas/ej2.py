'''Crear una lista con 100 números aleatorios, luego se debe generar dos listas
más: una que contenga los números pares de la primera y otra los impares'''

import random

lista_magica = []
lista_par = []
lista_impar = []

for i in range(100):
    aux = random.randint(0, 9)
    lista_magica.append(aux)
    if(aux%2 == 0):
        lista_par.append(aux)
    else:
        lista_impar.append(aux)

print("Global: ",lista_magica)
print("Par: ",lista_par)
print("Impar: ",lista_impar)  