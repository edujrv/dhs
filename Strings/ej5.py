''' 5. Recibir por teclado un string y contar la cantidad de mayúsculas, 
minús-culas y símbolos que se encuentran en la misma '''

minusculas = 0
mayusculas = 0
simbolos = 0


frase = input("Ingrese una frase: ")

for i in frase:
    if ( i >= 'a' and i <= 'z'):
        minusculas += 1
    elif ( i >= 'A' and i <= 'Z'):
        mayusculas += 1
    else: 
        if i == " ":
            continue
        simbolos += 1
        
print("La cantidad de mayusculas es ", mayusculas, ", de minusculas es ", minusculas, " y de simbolos es ", simbolos)