#  5. partir del diccionario del ejercicio anterior, 
# modificar el número de legajo y agregar dos materias 
# nuevas en la lista de materias

estudiante = {"Nombre": '', "Apellido":'' , "Legajo":'' , "Materias":''}

# estudiante['Nombre'] = 'Klan'

print("Ingrese los datos del estudiante")
for i in estudiante:
    print(i, ": ", end='')
    aux = input()
    estudiante[i] = aux

estudiante['Materias'] = estudiante['Materias'].split(', ')

print("Estudiante original\n", estudiante)

estudiante["Legajo"] = '545564'
estudiante["Materias"].append("desarrollo de memes 2")
estudiante["Materias"].append("analisis de analiticos analistas")
# estudiante["Materias"] += "desarrollo de memes 2, analisis de analiticos analistas".split(', ')

print("Estudiante modificado\n",estudiante)