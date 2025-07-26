#tblero de ajedrez
for fila in range(8):
    linea = ""
    for col in range(8):
        if (fila + col) % 2 == 0:
            linea += "#"
        else:
            linea += "✨"
    print(linea)
