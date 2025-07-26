#Crea un ciclo infinito que reciba una frase por teclado y verifique si la frase es palíndromo. La ejecución termina si la frase ingresada contiene la palabra salir


while True:
    frase = input("Escribe una frase (o escribe 'salir' para terminar): ")
    
    if "salir" in frase.lower():
        print("👋 Saliendo del programa...")
        break

    # Limpiar la frase (sin espacios ni mayúsculas)
    frase_limpia = frase.replace(" ", "").lower()
    
    if frase_limpia == frase_limpia[::-1]:
        print("Es un palíndromo")
    else:
        print("No es un palíndromo")

