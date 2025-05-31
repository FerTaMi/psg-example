#ejercicio 3
# tarjeta = True si se introduce tarjeta válida
# huella = True si se introduce huella dactilar

tarjeta = True
huella = False

# Caso 1: no tarjeta, no huella
puerta = tarjeta != huella
print("Caso 1")
print("Tarjeta:", tarjeta)
print("Huella:", huella)
print("Puerta se abre:", puerta)
print("")

# Caso 2: no tarjeta sí huella

tarjeta = False
huella = True
puerta = tarjeta != huella
print("Caso 2")
print("Tarjeta:", tarjeta)
print("Huella:", huella)
print("Puerta se abre:", puerta)
print("")

# Caso 3: sí tarjetano huella

tarjeta = True
huella = False
puerta = tarjeta != huella
print("Caso 3")
print("Tarjeta:", tarjeta)
print("Huella:", huella)
print("Puerta se abre:", puerta)
print("")

# Caso 4: sí tarjeta sí huella
tarjeta = True
huella = True
puerta = tarjeta != huella
print("Caso 4")
print("Tarjeta:", tarjeta)
print("Huella:", huella)
print("Puerta se abre:", puerta)