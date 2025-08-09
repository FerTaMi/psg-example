#saldo = 500

#monto = int(input("Ingrese el monto a retirar: "))

#if monto > saldo
#    raise Exception("No hay fondos suficiente")

#if monto > 1000:
#    raise Exception("Monto excede el limite permitido")
    
#print("Retiro exitoso")

class FondosInsuficientesError(Exception):
    pass

saldo = 500

monto = int(input("Ingrese el monto a retirar: "))

if monto > saldo:
    raise FondosInsuficientesError("No hay fondos suficientes")

if monto > 1000:
    raise Exception("Monto excede el limite permitido")
    
print("Retiro exitoso")

