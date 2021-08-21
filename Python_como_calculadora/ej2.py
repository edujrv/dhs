'''2. Realizar un programa que calcule el desglose mínimo en billetes
y monedas de una cantidad exacta de pesos. 
Hay billetes de $1000, $500, $200, $100 y monedas de $10, $5, $2 y $1.
El desglose se realiza del más grande al más pequeño.'''

monto = int(input("Ingrese un monto a desglosar"))
dinero = monto
mil = 0
quinientos = 0
doscientos = 0
cien = 0
diez = 0 
cinco = 0
dos = 0
uno = 0

while (dinero != 0):
    if(dinero >= 1000):
        dinero -= 1000
        mil += 1
    elif (dinero >= 500):
        dinero -= 500
        quinientos += 1
    elif (dinero >= 200):
        dinero -= 200
        doscientos += 1
    elif (dinero >= 100):
        dinero -= 100
        cien += 1
    elif (dinero >= 10):
        dinero -= 10
        diez += 1
    elif (dinero >= 5):
        dinero -= 5
        cinco += 1
    elif (dinero >= 2):
        dinero -= 2
        dos += 1
    elif (dinero >= 1):
        dinero -= 1
        uno += 1
    elif(dinero == 0):
        break
    

print("Su monto de $", monto ," se desglosa en: \n", mil," billetes de mil pesos\n ", quinientos, " billetes de quinientos pesos\n",  
doscientos ," billetes de doscientos pesos\n",  cien," billetes de cien pesos\n",  diez," monedas de diez pesos\n",  cinco ," monedas de cinco pesos\n", 
 dos," monedas de dos pesos\n", uno," monedas de un peso\n",)  