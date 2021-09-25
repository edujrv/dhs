'''
uego de instalar packete externo time utilizando Anaconda (link a docu-mentación), crear un decorador que permita medir el tiempo de ejecuciónde una función.
Luego, se debe implementar una función que permita multiplicar elementoa elemento los siguientes objetos:
Dos listas del 100.000 elementos enteros
Dos tuplas del 100.000 elementos enteros
Dos listas del 100.000 elementos flotantes
Dos tuplas del 100.000 elementos flotantes
'''
#TODO: El tiempo te lo debo.

def decorador(function):
    def function_to_return(arg):
        print("Empezo")
        function(arg)
        print("Termino")
    return function_to_return

@decorador
def multiplicar(lista):
    producto = 1
    for elemento in lista:
        producto = elemento * producto
    print("El producto es: ", producto)
    return 0


lista = [1,5,4,3,54,65,5,4,3,65,5,3,24,2,23,4,76]
multiplicar(lista)