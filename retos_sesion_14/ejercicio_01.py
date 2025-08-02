#Crea una función que reciba una lista de calificaciones y devuelva el promedio de las mismas.
#Las calificaciones son: 50, 75, 80, 91, 70

def calcular_promedio(calificaciones):
    suma = sum(calificaciones)
    cantidad = len(calificaciones)
    promedio = suma / cantidad
    return promedio

# Lista de calificaciones
notas = [50, 75, 80, 91, 70]

# Llamar a la función y mostrar el resultado
resultado = calcular_promedio(notas)
print("El promedio es:", resultado)
