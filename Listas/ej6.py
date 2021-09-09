# 6. Diseñar un programa que tomando una lista de números enteros,
#  genere una nueva eliminando los números repetidos de la primera

# voy a usar un set porque son objetos unicos y con un objeto lista es un lio

numeros = []
lista_nueva = set()  # creo un set

print("Ingrese numeros y para terminar una letra")
while True:
    aux = input("-> ")
    if aux >= '0' and aux <='9':
        numeros.append(int(aux))
        lista_nueva.add(int(aux))
    else:
        break

print("La lista ingresada es")
print(numeros)

print("\nLa lista sin repetidos es")
print(lista_nueva)