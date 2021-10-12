'''
4. Construir una librería estática que contenga las funciones implementadas
en (2). Generar el proceso de linking con el programa principal. Extraer
conclusiones.

# primero creamos los .objeto
$ gcc -c sumar.c restar.c

# ahora los agrupamos en una libreria
$ ar rs libreria.a sumar.o restar.o

# ya teniendo esa libreria podemos hacer cambios en el main
$ gcc -c main.c
$ gcc main.o libreria.a


'''

