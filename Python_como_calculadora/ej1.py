''' 1. Dado dos números enteros imprimir por pantalla el producto de los mismos. 
Si el producto es más grande que 10000, imprimir su suma '''

entero1 = int(input("Ingrese un entero: \n"))
entero2 = int(input("Ingrese otro entero: \n"))
resultado = entero2 * entero1

if (resultado > 10000):
    print("La suma de los enteros ingresado es: ",entero1 + entero2)
else:
    print("El producto de los enteros ingresado es: ", resultado)