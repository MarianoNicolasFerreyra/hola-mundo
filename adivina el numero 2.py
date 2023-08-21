import random

def jugar_adivinanza():
    while True:
        numero_secreto = random.randint(1, 1000)
        intentos = 0

        print("¡Bienvenido al juego de adivinanzas!")
        print("Estoy pensando en un número del 1 al 1000. Adivina, tenes 10 intentos")

        while intentos < 10:
            try:
                intento = int(input("Tira fruta: "))
            except ValueError:
                print("Escribi bien bobi.")
                continue

            intentos += 1

            if intento < numero_secreto:
                print("El número secreto es mayor.")
            elif intento > numero_secreto:
                print("El número secreto es menor.")
            else:
                print(f"Mu bien. Adivinaste el numero {numero_secreto} en {intentos} intentos")
                break
        else:
            print(f"Agotaste tus 10 intentos. El número secreto era {numero_secreto}. ¡ALTO BOT!")

        jugar_nuevamente = input("¿Quieres jugar de nuevo? (s/n): ")
        if jugar_nuevamente.lower() != 's':
            print("nos vemos bro")
            break

if __name__ == "__main__":
    jugar_adivinanza()