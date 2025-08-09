#calculadora interactiva
#print("📟 Calculadora interactiva")
#while True:
#    num1 = input("Ingrese el primer número o 'salir': ")
#    if num1.lower() == "salir":
#        break
#    num2 = input("Ingrese el segundo número: ")
    
   
#    resultado_suma = num1 + num2  # Esto concatena strings, no suma
#    print("Suma:", resultado_suma)
#    print("Resta:", num1 - num2)  # Esto va a dar error 💥

# Calculadora interactiva (reto sesión 15)

while True:
    try:
        num1 = input("Ingrese el primer número (o 'salir'): ")
        if num1.lower() == "salir":
            print("Adiós 👋")
            break
        
        num2 = input("Ingrese el segundo número (o 'salir'): ")
        if num2.lower() == "salir":
            print("Adiós 👋")
            break

        num1 = float(num1)
        num2 = float(num2)

        # Operaciones
        suma = num1 + num2
        resta = num1 - num2
        multiplicacion = num1 * num2
        division = num1 / num2  # Puede dar ZeroDivisionError

        print("\n📊 Resultados:")
        print(f"{num1} + {num2} = {suma}")
        print(f"{num1} - {num2} = {resta}")
        print(f"{num1} × {num2} = {multiplicacion}")
        print(f"{num1} ÷ {num2} = {division}")

    except ValueError:
        print("💀 Error: Ingresa solo números o 'salir'.")
    except ZeroDivisionError:
        print("💀 Error: No se puede dividir entre cero.")
    except Exception as e:
        print(f"💀 Error inesperado: {e}")
