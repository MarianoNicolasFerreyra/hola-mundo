import random

def mostrar_tablero(tablero):
    for fila in tablero:
        print(" | ".join(fila))
        print("---------")

def verificar_ganador(tablero, jugador):
    for fila in tablero:
        if fila.count(jugador) == 3:
            return True

    for columna in range(3):
        if tablero[0][columna] == tablero[1][columna] == tablero[2][columna] == jugador:
            return True

    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador:
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        return True

    return False

def entrada_valida(fila, columna):
    return fila in [0, 1, 2] and columna in [0, 1, 2]

def obtener_entrada_usuario():
    while True:
        try:
            fila = int(input("Ingrese el número de fila (0-2): "))
            columna = int(input("Ingrese el número de columna (0-2): "))

            if not entrada_valida(fila, columna):
                print("Valor inválido. Ingrese un número entre 0 y 2.")
                continue

            return fila, columna
        except ValueError:
            print("Valor inválido. Ingrese un número entre 0 y 2.")

def jugar_tres_en_linea_bot():
    while True:
        tablero = [[" " for _ in range(3)] for _ in range(3)]
        jugador_actual = "X"
        juego_terminado = False

        while not juego_terminado:
            mostrar_tablero(tablero)

            if jugador_actual == "X":
                fila, columna = obtener_entrada_usuario()
            else:
                print("Turno del bot:")
                fila = random.randint(0, 2)
                columna = random.randint(0, 2)
                print("El bot eligió la fila", fila, "y la columna", columna)

            if tablero[fila][columna] == " ":
                tablero[fila][columna] = jugador_actual
                if verificar_ganador(tablero, jugador_actual):
                    mostrar_tablero(tablero)
                    if jugador_actual == "X":
                        print("Ganaste")
                    else:
                        print("Cómo te va a ganar un bot? ¡Jaja!")
                    juego_terminado = True
                elif all(all(casilla != " " for casilla in fila) for fila in tablero):
                    mostrar_tablero(tablero)
                    print("Empataste con un bot, ¡jaja!")
                    juego_terminado = True
                else:
                    jugador_actual = "O" if jugador_actual == "X" else "X"
            else:
                print("Esa casilla ya está ocupada. Intenta de nuevo.")

        opcion = input("¿Deseas jugar de nuevo? Ingresa 1 para volver a jugar o 2 para salir: ")
        if opcion == "2":
            print("Gracias por jugar. ¡Hasta luego!")
            break
        elif opcion != "1":
            print("Opción inválida. Saliendo del juego.")
            break

jugar_tres_en_linea_bot()
