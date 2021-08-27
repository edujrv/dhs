# Diseñar un programa permita la carga de dos matrices distintas de 3x3.
# Luego, se debe imprimir la suma y la multiplicación entre ambas

# inicio funcion de carga
def cargar_matriz():
    print("Cargue la matriz\n")
    matriz = []
    for i in range(3):
        aux = []
        print("fila ",i)
        for j in range(3):
            elemento = int(input("-> "))
            aux.insert(j, elemento)
        matriz.insert(i, aux)
    return matriz
# fin de funcion 

# inicio de funcion muestra
def mostrar_matriz(matriz):
    for i in range(3):
        print(matriz[i])
# fin de funcion

# inicio funcion de suma
def suma_matriz(matriz_uno, matriz_dos):
    matriz = []
    for i in range(3):
        aux_uno = matriz_uno[i]
        aux_dos = matriz_dos[i]
        aux_tres = []
        for j in range(3):
            aux = aux_uno[j] + aux_dos[j]
            aux_tres.insert(j, aux)
        matriz.insert(i, aux_tres)
    return matriz

# fin de funcion

# inicio funcion para devolver columnas de una matriz
def columnas(matriz):
    fila = []
    aux_uno = []
    aux_dos = []
    aux_tres = []
    col = []
    for i in range(3):
        fila = matriz[i]
        aux_uno.insert(i, fila[0])
        aux_dos.insert(i, fila[1])
        aux_tres.insert(i, fila[2])
    col.insert(0, aux_uno)
    col.insert(1, aux_dos)
    col.insert(2, aux_tres)
    return col
# fin funcion

# inicio funcion multiplicacion
def multiplicar_matriz(matriz_filas, matriz_col):
    matriz = []
    for k in range(3):
        aux_uno = []
        aux_dos = []
        aux_tres = []
        for i in range(3):
            aux = 0
            aux_uno = matriz_filas[k] 
            aux_dos = matriz_col[i]   
            for j in range(3):
                aux += aux_uno[j] * aux_dos[j]
            aux_tres.insert(i, aux) # aca se guardan las filas de la matriz final   
        matriz.insert(k, aux_tres)
    return matriz
          
#fila 0 * col 0 = m[0][0]   fila 0 * col 1 = m[0][1]   fila 0 * col 2 = m[0][2]
#fila 1 * col 0 = m[1][0]   fila 1 * col 1 = m[1][1]   fila 1 * col 2 = m[1][2]      
#fila 2 * col 0 = m[2][0]   fila 2 * col 1 = m[2][1]   fila 2 * col 2 = m[2][2]
# fin de funcion

matriz_uno = cargar_matriz()
matriz_dos = cargar_matriz()

print("Primera matriz: \n")
mostrar_matriz(matriz_uno)

print("Segunda matriz \n")
mostrar_matriz(matriz_dos)

matriz_suma = suma_matriz(matriz_uno, matriz_dos)
print("La suma de matrices es\n")
mostrar_matriz(matriz_suma)

# en multiplicar, mandar la matriz filas y las col de la otra.
print("La multiplicacion de matrices es\n")
matriz_col = []
matriz_col = columnas(matriz_dos) #quiero las columnas de esta matriz
#mostrar_matriz(matriz_col)

matriz_total = multiplicar_matriz(matriz_uno, matriz_col)
mostrar_matriz(matriz_total)