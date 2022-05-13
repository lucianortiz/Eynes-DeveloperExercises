import random

# Cargo matriz con numeros random del 1 al 5
def cargar(matriz):

    for i in range(5):
        matriz.append([0] * 5)
        
    for i in range(5):
        for j in range(5):
            matriz[i][j]= random.randint(1,5)

# Se muestra la matriz
def mostrar(matriz):
    for fila in matriz:
        print (fila)

# Verifico si en las filas hay secuencia de 4 numeros consecutivos
def verificacion_horizontal(matriz):
    '''
    >>> verificacion_horizontal([[3, 2, 3, 5, 4],[3, 3, 2, 1, 2],[1, 1, 5, 4, 5],[1, 5, 2, 4, 2],[2, 2, 3, 5, 4]])
    No hay coincidencia horizontal
    False

    >>> verificacion_horizontal([[4, 5, 1, 2, 3],[2, 2, 3, 4, 5],[3, 2, 3, 4, 3],[1, 3, 1, 1, 2],[1, 1, 5, 2, 4]])
    Coincidencia horizontal empieza en la posicion [2,2] y termina en [2,5]
    True

    >>> verificacion_horizontal([[1, 2, 3, 4, 5],[2, 2, 3, 4, 5],[3, 2, 3, 4, 3],[1, 3, 1, 1, 2],[1, 1, 5, 2, 4]])
    Coincidencia horizontal empieza en la posicion [1,1] y termina en [1,4]
    True
    '''
    i=0
    bandera= False # Para cortar el bucle en caso que 
    
    while i < len(matriz) and bandera != True:
        if matriz[i][1] == matriz[i][2]-1 == matriz[i][3]-2: # Si los 3 nums del medio no son consecutivos, no tiene sentido ver los valores de los extremos
            if matriz[i][0] == matriz[i][1]-1: # Chequeo extremos
                bandera= True
                li=1 # Indico cual es la columna en la que arranca y termina la secuencia
                ls=4 
            elif matriz[i][3] == matriz[i][4]-1:
                bandera= True
                li=2
                ls=5
        i+=1

    if bandera == False:
        print("No hay coincidencia horizontal")
    else:
        print(f"Coincidencia horizontal empieza en la posicion [{i},{li}] y termina en [{i},{ls}]")

    return bandera

# Verifico si en las columnas hay secuencia de 4 numeros consecutivos
def verificacion_vertical(matriz):

    '''
    >>> verificacion_vertical([[3, 2, 3, 5, 4],[3, 3, 2, 1, 2],[1, 1, 5, 4, 5],[1, 5, 2, 4, 2],[2, 2, 3, 5, 4]])
    No hay coincidencia vertical

    >>> verificacion_vertical([[1, 2, 3, 1, 5],[2, 2, 3, 2, 5],[3, 2, 3, 3, 3],[1, 3, 1, 4, 2],[1, 1, 5, 2, 4]])
    Coincidencia vertical empieza en la posicion [1,4] y termina en [4,4]
    '''

    i=0
    bandera= False

    while i < len(matriz) and bandera != True:
        if matriz[1][i] == matriz[2][i]-1 == matriz[3][i]-2:
            if matriz[0][i] == matriz[1][i]-1:
                bandera= True
                li=1 # Indico cual es la fila en la que arranca y termina la secuencia
                ls=4
            elif matriz[3][i] == matriz[4][i]-1:
                bandera= True
                li=2
                ls=5
        i+=1

    if bandera == False:
        print("No hay coincidencia vertical")
    else:
        print(f"Coincidencia vertical empieza en la posicion [{li},{i}] y termina en [{ls},{i}]")
        
 # Verificacion de secuencia de numeros consecutivos. En caso que no haya verificacion horizontal se pasa a la vertical.
def verificar(matriz):
    if verificacion_horizontal(matriz) == False:
        verificacion_vertical(matriz)

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    matriz= []
    cargar(matriz)
    mostrar(matriz)
    verificar(matriz)
    test()