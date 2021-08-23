'''Considerando dos listas de números enteros:
De cada una de las listas imprimir los números divisibles por 5
#Calcular e imprimir la suma vectorial de ambas
#Calcular e imprimir el producto punto'''

def cargar_lista():
    lista = []
    while True:
        aux = input("Ingrese un entero: ")
        if aux >= '0' and aux <= '9': 
            lista.append(int(aux))
        else: 
            break
    return lista

def divisibilidad(lista):
    print("Numeros divisibles por 5 en lista\n")
    for i in lista:
        if (int(i) % 5 == 0):
            print(". ", i)

def suma_vectorial(lista_1, lista_2):
    suma = 0
    producto = 0
    producto_punto = 0
    print("La suma vectorial es: \n")
    for i in range(len(lista_1)):
        suma = lista_1[i] + lista_2[i]
        print(". ",suma)
        producto = lista_1[i] * lista_2[i]
        producto_punto += producto
    print("El producto punto es: ", producto_punto)

print("Primera lista\n")
lista_uno = cargar_lista()
print("Segunda lista\n")
lista_dos = cargar_lista()

divisibilidad(lista_uno)
divisibilidad(lista_dos)

suma_vectorial(lista_uno, lista_dos)
