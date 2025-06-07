
texto = input("Escribe una frase: ")
sin_espacios = texto.replace(" ", "")
minúsculas = sin_espacios.lower()
invertido = minúsculas[::-1]

es_palindromo = minúsculas == invertido

print("¿Es palíndromo?", es_palindromo)