'''Dado un rango de 10 números enteros, iterar desde el primero al último y
en cada iteración imprimir:
Valor actual
Valor anterior
Valor siguiente
Suma acumulada
Nota: se debe usar range() para generar el rango de números'''

lista = []
suma = 0

for i in range(10):
    lista.append(int(input("Ingrese un numero: ")))

for i in range(10):
    suma += lista[i]
    if (i == 0):
        print("Valor actual: ", lista[i], "Valor siguiente: ", lista[i+1], "Suma acumulada: ", suma)
    elif (i == 9):
        print("Valor actual: ", lista[i], "Valor anterior: ", lista[i-1], "Suma acumulada: ", suma)
    else:
        print("Valor actual: ", lista[i], "Valor siguiente: ", lista[i+1], "Valor anterior: ", lista[i-1], "Suma acumulada: ", suma)
