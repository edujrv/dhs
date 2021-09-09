# Crear una lista que contenga en su interior 27 listas, 
# asociadas cada una a una letra del alfabeto español.
# Luego tomar por teclado 32 palabras y añadirlas 
# cada una a la lista co-rrespondiente a su primera letra

# alfabeto = [[]]*27
alfabeto = [[] for i in range(27) ] # para que cada lista sea una referencia distinta

for i in range(26): # xq no toma ñ
    alfabeto[i].append(chr(i+97))  # chr -> funcion inversa de ord
print(alfabeto)

print("Ingrese palabras")
for i in range(5): # cambiar a 32 palabras si quieres
    aux = input("-> ")
    for i in range(26):
        if aux.startswith(alfabeto[i][0]) == True:
            alfabeto[i].append(aux)
     

print("La lista quedo de la siguiente forma\n", alfabeto)