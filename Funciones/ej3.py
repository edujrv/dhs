'''
Escribir una función que reciba un string y luego calcule y retorne lacantidad de letras mayúsculas y minúsculas presentes en la misma
'''

def calcular_mays_y_mins(frase):
    mins = 0
    mays = 0

    for letra in frase:
        if (letra == " "): 
            continue
        elif (letra > "a" and letra < "z"):
            mins = mins + 1
        elif(letra > "A" and letra < "Z"):
            mays = mays + 1
    
    return (mays,mins)


string = input("Ingrese un string: ")
tupla = calcular_mays_y_mins(string)
print(string, " Tiene ", tupla[0], " mayusculas y", tupla[1], " minusculas")