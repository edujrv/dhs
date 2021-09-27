'''7. Escribir un programa en Python que lea información de texto de cuatro
archivos distintos, la imprima por pantalla y luego la guarde en un archivo
distinto.'''

resultado = open("Archivos//resultado.txt",mode = "w", encoding = "utf-8")
try:

    file = open("Archivos//text1.txt",mode = "r", encoding = "utf-8")
    lines = file.readlines()
    for line in lines:
        resultado.write(line)
    resultado.write("\n")
    
    file = open("Archivos//text2.txt",mode = "r", encoding = "utf-8")
    lines = file.readlines()
    for line in lines:
        resultado.write(line)
    resultado.write("\n")

    file = open("Archivos//text3.txt",mode = "r", encoding = "utf-8")
    lines = file.readlines()
    for line in lines:
        resultado.write(line)
    resultado.write("\n")
    
    file = open("Archivos//text4.txt",mode = "r", encoding = "utf-8")
    lines = file.readlines()
    for line in lines:
        resultado.write(line)

    resultado.close
    resultado = open("Archivos//resultado.txt","r") 
    lines = resultado.readlines()
    for line in lines:
        print(line)

except:
    print("No se pudo abrir el archivo")
