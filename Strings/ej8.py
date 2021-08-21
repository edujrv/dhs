sentence = input("Ingresar oracion: ")
num = int(input("Ingresar numero: "))

aux = 0
countMenores = 0
countIguales = 0
countMayores = 0

for x in sentence:
    if (x != ' '):
        aux += 1
    else:
        if (aux > num):
            countMayores += 1
        if (aux < num):
            countMenores += 1
        if (aux == num):
            countIguales += 1 
        aux = 0
aux += 1
if (aux > num):
    countMayores += 1
if (aux < num):
    countMenores += 1
if (aux == num):
    countIguales += 1 

print("Palabras iguales",countIguales)
print("Palabras menores",countMenores)
print("Palabras mayores",countMayores)
   
