#deportiva
deportiva = ["Short", "Playera", "Sudadera", "Tenis", "Short", "Calcetines"]

#formal
formal = ["Saco", "Corbata", "Pantalón de vestir", "Zapatos", "Calcetines"]

# Unimos ambas listas y eliminamos repetidos usando set
combinada = set(deportiva + formal)

#conjunto combinado
print("Tienda con ropa combinada:")
print(combinada)
