'''
5. Repetir el procedimiento del item anterior para una librería estática. Ins-
talarla en el sistema y extraer conclusiones sobre el tamaño del archivo
resultante


$ gcc -Wall -fPIC -c sumar.c
$ gcc -Wall -fPIC -c restar.c
$ gcc -Wall -c main.c
# con esto genero los .o

$ ld -o libreriadhs.so sumar.o restar.o -shared
#tenemos la libreria dinamica; com gcc en lugar de ld anda tambien

$ sudo cp libreriadhs.so /usr/lib/libreriadhs.so $ldconfig
# y ahora la movemos a /usr/lib no me preguntes xq pero es asi

$ gcc -o example main.o -I libreriadhs
$ ./example 
#generamos el ejecutable y c'est fini

'''