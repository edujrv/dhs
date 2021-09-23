# 4. Crear un diccionario llamado estudiante y luego la siguiente estructura:
#
# Nombre: string
# Apellido: string
# Legajo: string
# Materias que cursa: lista de strings
# 
# Cargar valores e imprimirlo por pantalla

lista = []
estudiante = {"Nombre": '', "Apellido":'' , "Legajo":'' , "Materias":''}

estudiante['Nombre'] = 'Klan'

print("Ingrese los datos del estudiante")
for i in estudiante:
    print(i, ": ", end='')
    aux = input()
    estudiante[i] = aux

# estudiante.update(Materias=estudiante.get('Materias').split(', '))
estudiante['Materias'] = estudiante['Materias'].split(', ')

print(estudiante)

################################################################
'''
estudiante = {}

estudiante['Nombre'] = input('Introducza un nombre: ')
estudiante['Apellido'] = input('Introducza un apellido: ')
estudiante['Legajo'] = input('Introducza un legajo: ')
estudiante['Materias'] = input(
    'Introducza la lista de materias que cursa (separadas por coma): ').split(', ')

print(estudiante)
'''