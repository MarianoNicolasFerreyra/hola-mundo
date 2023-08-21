def mostrar_tablero(tablero):
    for fila in tablero:
        print(" | ".join(fila))
        print("---------")


def hay_empate(tablero):
    for fila in tablero:
        for casilla in fila:
            if casilla == " ":
                return False
    return True


def jugar_tres_en_linea():
    while True:
        tablero = [[" " for _ in range(3)] for _ in range(3)]
        jugador_actual = "X"
        juego_terminado = False

        while not juego_terminado:
            mostrar_tablero(tablero)
            try:
                fila = int(input("Ingrese el número de fila (0-2): "))
                columna = int(input("Ingrese el número de columna (0-2): "))

                if fila not in [0, 1, 2] or columna not in [0, 1, 2]:
                    print("Valor inválido. Ingrese un número entre 0 y 2.")
                    continue

                if tablero[fila][columna] == " ":
                    tablero[fila][columna] = jugador_actual
                    if (tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador_actual or
                            tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador_actual or
                            tablero[fila][0] == tablero[fila][1] == tablero[fila][2] == jugador_actual or
                            tablero[0][columna] == tablero[1][columna] == tablero[2][columna] == jugador_actual):
                        mostrar_tablero(tablero)
                        print("El jugador", jugador_actual, "ganó")
                        juego_terminado = True
                    elif hay_empate(tablero):
                        mostrar_tablero(tablero)
                        print("¡Empate!")
                        juego_terminado = True
                    else:
                        jugador_actual = "O" if jugador_actual == "X" else "X"
                else:
                    print("Esa casilla ya está siendo usada, introduzca otra")
            except ValueError:
                print("Valor inválido. Ingrese un número entre 0 y 2.")

        opcion = input(
            "¿Quiere jugar de vuelta? Ingrese 1 para volver a jugar, si no lo desea, ingrese otro parámetro: ")
        if opcion != "1":
            print("Gracias por jugar. ¡Chau!")
            break


jugar_tres_en_linea()
