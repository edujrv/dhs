# Diseñar un programa que dada una lista con números positivos y negativos,
# sustituya los negativos por cero

frase = []
print("Ingrese numeros positivos y negativos; letra para terminar: ")

while True:
    aux = input(" -> ")
    if aux >= '0' and aux <= '9' or aux.startswith("-") == True:
        frase.append(aux)
    else:
        break

print("La lista es: ", frase)

nueva_lista = []
for i in frase:
    if i.startswith("-") == True:
        nueva_lista.append("0")
    else:
        nueva_lista.append(i)
     
print("La nueva lista es: ",nueva_lista)