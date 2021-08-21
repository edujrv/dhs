''' Diseñar un programa que, dados cinco puntos en el plano, determine cuál
de los cuatro últimos es más cercano al primero. '''

import math
puntos = []
distancia = 0
x_cercano = 0
y_cercano=0

for k in range(5):
    print("\n Punto \n" , k)
    x = int(input("\nIngrese la coordenada X del punto: "))
    y = int(input("\nIngrese la coordenada Y del punto: "))
    puntos.append([x,y])


x = puntos[0][0]
y = puntos[0][1]

for i in range(1,5):
    xprima = x - puntos[i][0]
    yprima = y - puntos[i][1]
    dist = math.sqrt(pow(xprima,2) + pow(yprima,2))

    if (distancia > dist or distancia == 0):
        distancia = dist
        x_cercano = puntos[i][0]
        y_cercano = puntos[i][1]

print("\nLa distancia mas corta al punto [" , x , "][", y ,"] es: ", distancia)
print("\nEn el punto: [" , x_cercano , "][", y_cercano,"]")