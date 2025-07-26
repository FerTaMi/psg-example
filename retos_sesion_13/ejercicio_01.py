# Primeros dos valores
lucas = [2, 1]

# Generamos 20 valores
while len(lucas) < 20:
    siguiente = lucas[-1] + lucas[-2]
    lucas.append(siguiente)

print("Sucesión de Lucas:")
print(lucas)
