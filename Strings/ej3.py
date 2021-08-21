'''Modificar el programa para que reciba dos números enteros que permitan
definir el comienzo y el fin de caracteres a extraer del string original'''

frase = str(input("Ingrese una frase y un numero: "))
numero = ""
cond = False

for i in frase:

    if(not cond):
        if (i >= "0" and i<= "9"):
            cond = True
            continue

    elif(cond):
        if (i >= "0" and i<= "9"):
            cond = False
        else:
            numero = numero + i

print(numero)