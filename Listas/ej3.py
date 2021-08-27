# 3)Ingresar un string por teclado y hacer dos listas:
#  una que contenga las letras mayúsculas de la palabra
#  y otra las minúsculas

str = input("Ingrese una cadena pls: ")
lista_uno = ["MAYUSCULAS"]
lista_dos = ["minusculas"]

for i in str:
    if ord(i) >= 97 and ord(i) <= 122:
        lista_dos.append(i)
    elif ord(i) >= 65 and ord(i) <= 90:
        lista_uno.append(i)

print(lista_uno,'\n',lista_dos)