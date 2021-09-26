'''
Diseñar un programa que a partir de una lista genere otra con sólo losnúmeros positivos. Utilizar filter()
'''

lista = [-32,56,-4,-345,-7,4,3,-423,6,5,-63,-54,3,6,4345,-45,-654,2,8,-90,78,8,-98,10,7,-65,45,8]

solo_positivos = list (filter(lambda x: (x > 0), lista))

print(solo_positivos)