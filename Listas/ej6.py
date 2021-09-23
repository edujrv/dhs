#Diseñar un programa que tomando una lista de números enteros, genere
#una nueva eliminando los números repetidos de la primera

lista = []
listaNueva = []

for i in range(10):
    aux = input("Ingrese el numero a agregar en la lista o 'S' para terminar la carga:\n")
    if(aux == "S"):
        break
    else:
        lista.append(int(aux))

print("\n->Tu lista orignial es:   ->"+str(lista))

i == 0
aux = 0
for i in range(len(lista)):
    if i == 0:
        listaNueva.append(int(lista[i]))
        continue
    else:
        for j in range(len(listaNueva)):
            if lista[i] == listaNueva[j]:
                break
            if j == (len(listaNueva)-1):
                listaNueva.append(lista[i])

print("\n->Tu lista nueva es:   ->"+str(listaNueva))


    

   