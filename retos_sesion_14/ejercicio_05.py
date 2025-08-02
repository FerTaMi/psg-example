#Crear una función que reciba una cadena y devuelva la cantidad de vocales que tiene.

def contar_vocales(texto):
    vocales = "aeiouAEIOU"
    cantidad = 0

    for letra in texto:
        if letra in vocales:
            cantidad += 1

    return cantidad

# Probar la función con algunas frases
def probar_contar_vocales():
    frases = [
        "Hola mundo",
        "Python La Paz",
        "Estoy aprendiendo",
        "BCDFG",  # sin vocales
        "AEIOUaeiou",  # todas vocales
    ]

    for frase in frases:
        print(f"La frase: '{frase}' tiene {contar_vocales(frase)} vocales")

probar_contar_vocales()
