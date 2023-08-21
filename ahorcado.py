import random

AHORCADO = ['''
      +---+
      |   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
    =========''']
palabras = 'valoracion aprender python comida juego web imposible variable fue muy complicado escribir esto curso volador cabeza reproductor mirada le pedimos a chatgpt hacer los dibujos escritor billete lapicero celular revista gratuito disco voleibol anillo estrella hola me llamo nicolas ferreyra ojala estés leyendo esto'.split()

def buscarPalabraAleat(listaPalabras):
    palabrarandom = random.randint(0, len(listaPalabras) - 1)
    return listaPalabras[palabrarandom]

def displayBoard(AHORCADO, letraIncorrecta, letraCorrecta, palabraSecreta):
    print(AHORCADO[len(letraIncorrecta)]) #len lee lo q ingresaste, su longitud, caracteres, etcetc
    print("")
    fin = " "
    print('Letras incorrectas:', fin)
    for letra in letraIncorrecta:
        print(letra, fin)
    print("")
    espacio = '_' * len(palabraSecreta)
    for i in range(len(palabraSecreta)):   #recorre cada letra
        if palabraSecreta[i] in letraCorrecta:   #si la letra ingresada ya fue adivinada
            espacio = espacio[:i] + palabraSecreta[i] + espacio[i + 1:]   #actualiza la lista de letras adivinadas
    for letra in espacio:
        print(letra, fin)
    print("")


def elijeLetra(algunaletraxd):
    while True:
        print('Adivina una letra:')
        letra = input()
        letra = letra.lower()
        if len(letra) != 1:   #se comprueba el largo de la palabra
            print('Introduce una sola letra.')
        elif letra in algunaletraxd:
            print('Ya elegiste esta, usá otra')
        elif letra not in 'abcdefghijklmnopqrstuvwxyz':
            print('Sólo se permiten letras.')
        else:
            return letra   #finaliza una función y devuelve un valor


def jugar_ahorcado():
    print('Quieres jugar de nuevo? (Si o No)')
    return input().lower().startswith('s')


print('A H O R C A D O')
letraIncorrecta = ""
letraCorrecta = ""
palabraSecreta = buscarPalabraAleat(palabras)
finJuego = False
while True:
    displayBoard(AHORCADO, letraIncorrecta, letraCorrecta, palabraSecreta)   #muestra el estado del juego
    letra = elijeLetra(letraIncorrecta + letraCorrecta)
    if letra in palabraSecreta:
        letraCorrecta = letraCorrecta + letra
        letrasEncontradas = True
        for i in range(len(palabraSecreta)):
            if palabraSecreta[i] not in letraCorrecta:
                letrasEncontradas = False
                break
        if letrasEncontradas:
            print('bien, la palabra correcta era esa "' + palabraSecreta + '" ganaste')
            finJuego = True
    else:
        letraIncorrecta = letraIncorrecta + letra
        if len(letraIncorrecta) == len(AHORCADO) - 1:
            displayBoard(AHORCADO, letraIncorrecta, letraCorrecta, palabraSecreta)
            print('!\nDespues de ' + str(len(letraIncorrecta)) + ' letras erroneas y ' + str(   #str transforma valores en cadenas
                len(letraCorrecta)) + ' letras correctas, la palabra era "' + palabraSecreta + '"')
            finJuego = True
    if finJuego:
        if jugar_ahorcado():
            letraIncorrecta = ""
            letraCorrecta = ""
            finJuego = False
            palabraSecreta = buscarPalabraAleat(palabras)
        else:
            break