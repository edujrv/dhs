'''
Escribir un programa que partiendo de una lista de números enteros, los clasifique en dos listas distintas: 
una con los números pares y otra con los impares. Resolver utilizando lambdas
'''    


numeros = [1,3,6,5,4,3,6,7,8,5,3,75,4,2]

numeros_pares = list (filter(lambda x: (x % 2 == 0), numeros))
numeros_impares = list (filter(lambda x: (x % 2 != 0), numeros))

print("Lista original: ", numeros, "\n Lista de los pares: ", numeros_pares, "\n Lista de los impares: ", numeros_impares)