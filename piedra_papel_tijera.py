import random

def jugar_piedra_papel_tijera():
    while True:
        a = int(input("Elija 1 de estos 3 elementos: 1 = Piedra, 2 = Papel, 3 = Tijera: "))

        if a < 1 or a > 3:
            print("Valor no existente, elija uno que si exista.")
            continue

        b = random.randint(1, 3)
        print(b)

        if a == 1 and b == 3:
            print("¡Ganaste! Piedra le gana a tijera")
        elif a == 1 and b == 2:
            print("¡Perdiste! Piedra no le gana a papel")
        elif a == 1 and b == 1:
            print("¡Empate!")
        elif a == 2 and b == 1:
            print("¡Ganaste! Papel le gana a piedra")
        elif a == 2 and b == 2:
            print("¡Empate!")
        elif a == 2 and b == 3:
            print("¡Perdiste! Papel no le gana a tijera")
        elif a == 3 and b == 1:
            print("¡Perdiste! Tijera no le gana a piedra")
        elif a == 3 and b == 2:
            print("¡Ganaste! Tijera le gana a papel")
        elif a == 3 and b == 3:
            print("¡Empate!")

        while True:
            opcion = input("¿quiere jugar de nuevo? Ingresa 1 para volver a jugar, o 2 para salir: ")
            if opcion not in ['1', '2']:
                print("valor no existente. Elija uno que si exista.")
            else:
                break

        if opcion == '2':
            break

jugar_piedra_papel_tijera()
