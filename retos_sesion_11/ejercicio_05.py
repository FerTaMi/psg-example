#diccionario inicial del arca
arca = {
    "🐶": 2,
    "🐱": 2,
    "🐯": 2,
    "🐵": 2,
    "🦄": 0,
    "🦒": 1
}

#añadir 3 especies más al arca
arca.update({
    "🦊": 2,
    "🐸": 2,
    "🐢": 2
})

#mostrar la lista de animales
print("Animales en el arca:")
animales_iter = iter(arca)  # Creamos un iterador sobre las claves
while True:
    try:
        especie = next(animales_iter)
        cantidad = arca[especie]
        print(f"{especie}: {cantidad}")
    except StopIteration:
        break

#verificar si el dragón está en el arca
print("\n¿Está el 🐲 dragón en el arca?")
print("🐲" in arca)  # False

#eliminar el unicornio
arca.pop("🦄")

#mdificar cantidad de 🦒 jirafa a 2
arca["🦒"] = 2

#vaciar el arca después del diluvio
arca.clear()

#arca vacía
print("\nArca después del diluvio:")
print(arca)  # {}


