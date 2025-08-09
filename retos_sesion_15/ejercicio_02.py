

#frutas_permitidas = ["🍅", "🍇", "🍈", "🍉", "🍊", "🍌", "🍍", "🍑"]
#canasta = []

#while True
#    fruta = input("Ingresa una fruta: ")

#    if fruta == "salir"
#        break

#    if fruta not in frutas_permitidas
#        raise Exception("Fruta no permitida")

#    canasta.append(fruta)

#print("Canasta:", canasta)


#

class FrutaNoValidaError(Exception):
    pass

frutas_permitidas = ["🍅", "🍇", "🍈", "🍉", "🍊", "🍌", "🍍", "🍑"]
canasta = []

while True:
    fruta = input("Ingresa una fruta (o 'salir' para terminar): ")

    if fruta == "salir":
        break

    if fruta not in frutas_permitidas:

        raise FrutaNoValidaError(f"La fruta '{fruta}' no es válida.")

    canasta.append(fruta)

print("Canasta:", canasta)
