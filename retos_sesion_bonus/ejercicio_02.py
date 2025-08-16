def obtener_aleatorio(semilla_texto):
    #seed
    seed = sum(ord(c) for c in semilla_texto)
    
    secreto = (seed * 7 + 13) % 100 + 1
    return secreto

def adivina(secreto):
    intentos = 0
    print("¿Qué número estoy pensando? (1-100)")
    while True:
        try:
            intento = int(input(f"Intento N° {intentos+1}: "))
            intentos += 1
            if intento == secreto:
                print("🎉 ¡Felicidades! Has adivinado el número!")
                break
            elif intento < secreto:
                print("El número es mayor.")
            else:
                print("El número es menor.")
        except ValueError:
            print("Por favor, ingresa un número válido.")
    print(f"Has adivinado el número en {intentos} intentos.\n")

def jugar():
    print("Bienvenido al juego de adivinanzas del Python Study Group 2025")
    print("="*63)
    nombre_jugador = input("¿Cuál es tu nombre?: ").strip()
    if not nombre_jugador:
        nombre_jugador = "Guest"
    print(f"Bienvenido, {nombre_jugador}!")
    print("="*63)
    print()
    
    while True:
        opcion = input("¿Quieres jugar? (s/n): ")
        if opcion.lower() != 's':
            break
        #aleatorio
        secreto = obtener_aleatorio(nombre_jugador)
        adivina(secreto)
    
    print("Gracias por participar!")
    print(f"Gracias {nombre_jugador.upper()} por ser parte del Python Study Group 2025! 🐍")

jugar()
