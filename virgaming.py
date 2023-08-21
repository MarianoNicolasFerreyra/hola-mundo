def mostrar_menu():
    print("Hola, ¿qué quieres jugar?:")
    print("1. Piedra, papel o tijera")
    print("2. Buscaminas")
    print("3. Ahorcado")
    print("4. Tres en línea")
    print("5. Tres en línea contra bot")
    print("6. Adiviná el número")
    print("7. Adiviná el número 2")

while True:
    mostrar_menu()
    opcion = input("Ingresa el número del juego (o '0' para salir): ")

    while opcion not in ['0', '1', '2', "3", "4", "5", "6", "7"]:
        print("Opción no válida. Por favor, elige una opción válida.")
        opcion = input("Ingresa el número del juego (o '0' para salir): ")

    if opcion == "0":
        break

    if opcion == "1":
        import piedra_papel_tijera

    elif opcion == "2":
        import buscaminas

    elif opcion == "3":
        import ahorcado

    elif opcion == "4":
        import tres_en_linea

    elif opcion == "5":
        import tres_en_linea_bot

    elif opcion == "6":
        import adiviná_el_número
        adiviná_el_número.adiviná_el_número()
    elif opcion == "7":
        import adivina_el_numero_2
        adivina_el_numero_2.jugar_adivina_el_numero_2()

    jugar_otro = input("¿Deseas jugar otro juego? Ingresa 's' para sí, o cualquier otra tecla para salir: ")
    if jugar_otro.lower() != "s":   #.lower es para que el valor sea indiferente entre minúsculas/mayúsculas
        break