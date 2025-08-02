#Crear una función anónima para obtener el valor absoluto de un número.
valor_absoluto = lambda numero: numero if numero >= 0 else -numero

def probar_valor_absoluto():
    ejemplos = [15, -8, 0, -100, 42]
    print("Probando valores:")
    for num in ejemplos:
        print(f"El valor absoluto de {num} es {valor_absoluto(num)}")

probar_valor_absoluto()
