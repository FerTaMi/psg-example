#tblero de ajedrez
patron = ["#*", "*#"]  # fila par, fila impar
fila_actual = 0

for _ in range(8):
    print(patron[fila_actual] * 4)
    # alternamos la fila
    fila_actual = 1 - fila_actual
