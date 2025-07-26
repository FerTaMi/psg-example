# Verificador de múltiplos de 7

while True:
    numero = int(input("Ingresa un número (0 para salir): "))
    
    if numero == 0:
        print("Saliste del verificador. Hasta luego.")
        break

    if numero % 7 == 0:
        print(f"{numero} es múltiplo de 7.")
    else:
        print(f"{numero} no es múltiplo de 7.")

