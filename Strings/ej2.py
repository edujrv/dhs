''' Solicitar el ingreso de un string por teclado junto a un número entero.
Se deben eliminar los caracteres comprendidos el inicio del string y el número
ingresado '''

frase = str(input("Ingrese una frase y un numero: "))
numero = ""
cond = False

for i in frase:
    if (i >= "0" and i<= "9"):
        cond = True
    if(cond):
        numero = numero + i

print(numero)
