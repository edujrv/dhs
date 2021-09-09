# 6. Modificar el ejercicio anterior para que la lista 
# de materias que cursa ahora sea un diccionario. 
# Es decir, cada materia tiene asociado un código

materia = dict()
estudiante = {"Nombre": '', "Apellido":'' , "Legajo":'' , "Materias":materia}

estudiante["Nombre"] = input("Ingrese su nombre: ")
estudiante["Apellido"] = input("Ingrese su apellido: ")
estudiante["Legajo"] = input("Ingrese su legajo: ")

while(1):
    aux = input("Ingrese la materia: ")
    if aux == ".":
        break
    materia[aux] = input("Ingrese el codigo de la materia: ")

estudiante["Materias"] = materia

print("Estudiante: ", estudiante)


