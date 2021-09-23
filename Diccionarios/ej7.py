# 7. A partir del diccionario del apartado anterior,
#  generar una lista con 10 diccionarios.
#  Cada uno de ellos representa un alumno distinto

planilla_alumnos = []

for j in range(3): # cambiar a 10 si te pinta 

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

    #print("Estudiante: ", estudiante)

    planilla_alumnos.append(estudiante)

    for k in planilla_alumnos:
        print(str(k)+"\n\n")

for k in range(3):
    print("Estudiante n° ", k, planilla_alumnos[k])