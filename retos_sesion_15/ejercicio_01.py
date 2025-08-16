# Calculadora interactiva

while True:
    num1 = input("Ingrese el primer número (o 'salir'): ")
    if num1.lower() == "salir":
        print("Adiós")
        break

    num2 = input("Ingrese el segundo número (o 'salir'): ")
    if num2.lower() == "salir":
        print("Adiós")
        break

    try:
        num1 = float(num1)
        num2 = float(num2)

        # Operaciones
        suma = num1 + num2
        resta = num1 - num2
        multiplicacion = num1 * num2

        print("\n Resultados:")
        print(f"{num1} + {num2} = {suma}")
        print(f"{num1} - {num2} = {resta}")
        print(f"{num1} × {num2} = {multiplicacion}")

        # División aparte
        if num2 != 0:
            print(f"{num1} ÷ {num2} = {num1 / num2}")
        else:
            print("No se puede dividir entre cero")

    except ValueError:
        print("Error: Ingresa solo números o 'salir'.")

