# 11) Detectar si una palabra ingresada es palindromo o no

str = input(" Ingrese una palabra: ")
indice_vuelta = len(str)-1
palindromo = 0

for i in str:
    if i == str[indice_vuelta]: #la letra es igual a su opuesto
        indice_vuelta-=1
        continue
    elif i != str[indice_vuelta]: #la letra es distinta
        palindromo=1
        break

if palindromo == 0:
    print("La palabra es palindromo")
else:
    print("La palabra no es palindromo")