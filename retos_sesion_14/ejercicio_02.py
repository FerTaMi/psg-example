#Crear una función que reciba dos números y una operación (suma, resta, multiplicación, división) y devuelva el resultado de la operación
#Ejemplo: calcular(10, 5, "+") debe devolver 15

def calcular(num1, num2, operacion):
    if operacion == "+":
        return num1 + num2
    elif operacion == "-":
        return num1 - num2
    elif operacion == "*":
        return num1 * num2
    elif operacion == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "❌ No se puede dividir entre cero"
    else:
        return "❓ Operación no válida"

# Ejemplo de uso
print("➕", calcular(10, 5, "+"))  # 15
print("➖", calcular(10, 5, "-"))  # 5
print("✖️", calcular(10, 5, "*"))  # 50
print("➗", calcular(10, 5, "/"))  # 2.0

