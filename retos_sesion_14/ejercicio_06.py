#Crear una función que reciba una lista de números y devuelva una lista con los números pares y otra lista con los números impares

def separar_pares_impares(numeros):
    pares = []
    impares = []

    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)

    return pares, impares

lista = [10, 23, 45, 6, 78, 11, 90, 2]
pares, impares = separar_pares_impares(lista)

print("Números pares:", pares)
print("Números impares:", impares)
