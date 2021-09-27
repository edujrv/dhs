'''3. Escribir un programa en Python que lea todas las lineas de un archivo de
texto'''

try:
    file = open("Archivos//file.txt",mode = "r", encoding = "utf-8")
    lines = file.readlines()
    print(lines)
    
except:
    print("No se pudo abrir el archivo")