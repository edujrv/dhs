#9. Diseñar un programa que recibiendo el nombre de un archivo, 
#   permita separar el nombre de su extensión
 
nombre = input("Ingrese el nombre del archivo con su extencion: ")
nombre_archivo = ""

for i in nombre:
    if (i == "."):
        break
    nombre_archivo += i

print(nombre_archivo)