# 12/13)Detectar si una palabra es alfabética

str = input("Ingrese una palabra: ")
flag = 0

palabra = str.lower() #unificamos en minusculas
for i in palabra:
    if ord(i) >= 97 and ord(i) <= 122:  # ord messirve para vel el ascii
        continue
    else:
        flag = 1
        break

if flag == 0:
    print("La palabra es alfabetica")
else:
    print("La palabra no es alfabetica")