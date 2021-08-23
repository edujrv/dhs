# 14. Luego de recibir por teclado un string que contenga letras y números,
# imprimir cada número contenido en el string y la suma de los mismos

frase = input("Ingrese una frase con letras y numeros: ")
suma = 0

for i in frase:
    if (i >= "0" and i<= "9"):
        print(". ", i)
        suma += int(i)

print(".La suma de los numeros es -> ", suma)
