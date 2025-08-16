
#2

frutas_permitidas = ["🍅", "🍇", "🍈", "🍉", "🍊", "🍌", "🍍", "🍑"]
canasta = []

while True:
    fruta = input("Ingresa una fruta (o 'salir' para terminar): ")

    if fruta.lower() == "salir":
        print("Adiós 👋")
        break

    if fruta not in frutas_permitidas:
        print(f"💀 La fruta '{fruta}' no está permitida. Intenta de nuevo.")
        continue   # vuelve al inicio del while

    canasta.append(fruta)
    print(f"✅ '{fruta}' agregada a la canasta.")

print("\n Canasta final:", canasta)

