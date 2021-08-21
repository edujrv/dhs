''' Recibir por teclado una frase de más de 80 caracteres.
 Luego, recibir también una segunda palabra. 
 Finalmente, imprimir cuantas veces aparece la
segunda palabra en la frase del comienzo''' 

frase = ""
while (len(frase) < 80):
    frase = input("Ingrese una frase de +80 caracteres:  ")
palabra = input("Ingrese una palabra:  ")

print("La palabra '",palabra,"' aparece ",frase.count(palabra)," veces.")
