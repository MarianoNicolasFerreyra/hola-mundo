import random

def tableroide(filas, columnas, num_minas):
    tablero = [[' ' for _ in range(columnas)] for _ in range(filas)]
    minas_colocadas = 0

    while minas_colocadas < num_minas:
        fila = random.randint(0, filas - 1)
        columna = random.randint(0, columnas - 1)

        if tablero[fila][columna] == ' ':
            tablero[fila][columna] = '*'
            minas_colocadas += 1

    return tablero

def mostrar_tablero(tablero):
    filas = len(tablero)
    columnas = len(tablero[0])

    print('    ' + '   '.join(str(i) for i in range(columnas)))
    print('  +' + '____' * columnas + '+')

    for i in range(filas):
        print(str(i) + ' | ' + ' | '.join(tablero[i]) + ' |')

    print('  +' + '____' * columnas + '+')

def minas_cerca(tablero, fila, columna):
    filas = len(tablero)
    columnas = len(tablero[0])
    contador = 0

    for i in range(max(0, fila - 1), min(fila + 2, filas)):
        for j in range(max(0, columna - 1), min(columna + 2, columnas)):
            if tablero[i][j] == '*':
                contador += 1

    return contador

def ver_casilla(tablero, tablero_visible, fila, columna):
    filas = len(tablero)
    columnas = len(tablero[0])

    if fila < 0 or fila >= filas or columna < 0 or columna >= columnas:
        return

    if tablero_visible[fila][columna] != ' ':
        return

    minas_alrededor = minas_cerca(tablero, fila, columna)
    tablero_visible[fila][columna] = str(minas_alrededor)

    if minas_alrededor == 0:
        for i in range(max(0, fila - 1), min(fila + 2, filas)):
            for j in range(max(0, columna - 1), min(columna + 2, columnas)):
                ver_casilla(tablero, tablero_visible, i, j)

def jugar_buscaminas():
    filas = 5
    columnas = 5
    num_minas = 7

    tablero = tableroide(filas, columnas, num_minas)
    tablero_visible = [[' ' for _ in range(columnas)] for _ in range(filas)]

    juego_terminado = False

    while not juego_terminado:
        mostrar_tablero(tablero_visible)
        fila = None
        columna = None

        while fila is None or fila < 0 or fila >= filas:
            fila_input = input('Ingrese la fila ')
            if fila_input == '':
                print("no existe, reintentelo")
            else:
                fila = int(fila_input)
                if fila < 0 or fila >= filas:
                    print("la fila no existe, intente ingresar una que esté entre 0 y 6.")

        while columna is None or columna < 0 or columna >= columnas:
            columna_input = input('Ingrese la columna ')
            if columna_input == '':
                print("no existe, intente de vuelta")
            else:
                columna = int(columna_input)
                if columna < 0 or columna >= columnas:
                    print("La columna ingresada no existe, Debe estar entre 0 y 6.")

        if tablero[fila][columna] == '*':
            print('perdiste')
            juego_terminado = True
        else:
            ver_casilla(tablero, tablero_visible, fila, columna)

            if all(all(casilla != ' ' for casilla in fila) for fila in tablero_visible):
                print('ganaste')
                juego_terminado = True

    opcion = input('¿querés jugar de nuevo? Ingrese 1 para volver a jugar, o 0 para salir: ')

    if opcion == '1':
        jugar_buscaminas()

jugar_buscaminas()