'''6. Modiﬁcar el programa anterior para que imprima la frecuencia de repeti-
ción de cada palabra en el archivo'''

palabras = dict()

try:
    file = open("Archivos//file.txt",mode = "r", encoding = "utf-8")
    lines = file.readlines()
    print(lines)

    for line in lines:
        for word in line.split(" "):
            if palabras.get(word) == None:
                palabras.update({word:1})
            else:
                palabras.update({word:palabras.get(word)+1})
 
    print(palabras)
    file.close()
    
except:
    print("No se pudo abrir el archivo")