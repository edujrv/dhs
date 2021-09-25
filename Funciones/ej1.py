'''
Crear una función en Python que imprima el valor y el ID de un objetorecibido en la misma. 
Luego crear un objeto lista, un entero y una tupla.Finalmente se deben imprimir estos tres objetos utilizando la función ysin hacerlo.
Extraer conclusiones sobre como las funciones en Python reciben parámetros.
'''

def imprimir_valor_e_ID(objetoRecibido):
    print("Valor del objeto recibido: ", objetoRecibido, "\n")
    print("ID del objeto recibido: ", id(objetoRecibido), "\n")


lista = [1,2,3,4,5]
entero = 5
tupla = (6,7,8,9,10)

print("\n-------------- L I S T A --------------\n")
print("Sin usar la funcion:\n")
print("Valor de la lista: ", lista, "\n")
print("ID de la lista: ", id(lista), "\n")
print("Usando la funcion:\n")
imprimir_valor_e_ID(lista)

print("\n-------------- E N T E R O --------------\n")
print("Sin usar la funcion:\n")
print("Valor de la entero: ", entero, "\n")
print("ID de la entero: ", id(entero), "\n\n")
print("Usando la funcion:\n")
imprimir_valor_e_ID(entero)

print("\n-------------- T U P L A --------------\n")
print("Sin usar la funcion:\n")
print("Valor de la tupla: ", tupla, "\n")
print("ID de la tupla: ", id(tupla), "\n")
print("Usando la funcion:\n")
imprimir_valor_e_ID(tupla)