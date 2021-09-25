'''
Escribir una función que acepte parámetros posicionales y kwargs. Luegola función debe imprimirlos indicando cómo fue recibido cada uno de losparámetros
'''
# TODO: oc.

a = "a"
b = "b"
c = "c"
d = "d"
e = "e"

def funcion_Parametrica_Impresionante_Atomica_Mundial(a,d = "dd", *va, **kw):
    print("Variable 'a': \n")
    print(a, " -> ", type(a), "\n")
    print("Variable 'd': \n")
    print(d, " -> ", type(d), "\n")
    print("Variable 'va': \n")
    print(va, " -> ", type(va), "\n")
    print("Variable 'kw': \n")
    print(kw, " -> ", type(kw), "\n")
    return

#funcion_Parametrica_Impresionante_Atomica_Mundial(a,d,b,c,e="Lituania")
#funcion_Parametrica_Impresionante_Atomica_Mundial(c,b,c,e="Lituania")
funcion_Parametrica_Impresionante_Atomica_Mundial(a=1)