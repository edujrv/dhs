'''5. Escribir un programa en Python lea el contenido de un archivo e identiﬁque
la palabra más larga de todo el archivo'''

longest = ""



try:
    file = open("Archivos//file.txt",mode = "r", encoding = "utf-8")
    lines = file.readlines()
    print(lines)

    for line in lines:
        for word in line.split(" "):
            if len(word) >= len(longest):
                longest = word
    print("La palabra mas larga del texto es: "+longest)

    file.close()
    
except:
    print("No se pudo abrir el archivo")