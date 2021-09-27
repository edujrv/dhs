'''
Diseñar un programa que sume tres listas. Utilizar map() y lambdas.
'''
    
def sum(x):
    sum = 0
    for i in x:
        sum += i
    return sum


lista1 = [1,2,3,4,5,56,6]
lista2 = [3,7,34,2,31,61,15]
lista3 = [4,8,6,23,4,5,5]



total = 0

listag = [lista1,lista2,lista3]
count = 0
suma = list (map(lambda x: sum(x), listag))
resultado = list (map(lambda x: total + x, suma))
print(total)