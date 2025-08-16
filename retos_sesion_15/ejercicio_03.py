#3

class FondosInsuficientesError(Exception):
    pass

saldo = 500

try:
    monto = int(input("Ingrese el monto a retirar: "))

    if monto > saldo:
        raise FondosInsuficientesError("No hay fondos suficientes.")

    if monto > 1000:
        raise Exception("Monto excede el límite permitido por transacción.")

    saldo -= monto
    print(f"Retiro exitoso. Nuevo saldo: {saldo}")

except ValueError:
    print("Error: Ingresa un número válido.")
except FondosInsuficientesError as e:
    print(e)
except Exception as e:
    print(e)

