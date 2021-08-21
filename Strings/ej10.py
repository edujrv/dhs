''' Diseñar un programa que lea dos cadenas de texto e imprima la mayor
coincidencia entre ambas'''

primera_cadena = input("Ingrese la primera cadena de txt:")
segunda_cadena = input("Ingrese la segunda cadena de txt:")
tercera_cadena = ""

primera_lista = primera_cadena.split()
segunda_lista = segunda_cadena.split()

for i in primera_lista:
    if(segunda_lista.count(i) != 0):
        if(segunda_lista.count(primera_lista(i)+" "+primera_lista(i+1)) != 0)
        continue
    else:
        tercera_cadena += i
    
print(tercera_cadena, sep=' ')
print(segunda_cadena)
  
