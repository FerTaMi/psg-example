# Diccionario inicial del arca
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

#Lista de animales en el arca
print("Animales en el arca:")
for especie, cantidad in arca.items():
    print(f"{especie}: {cantidad}")

#existe el 🐲 dragón en el arca?
print("\n¿Está el 🐲 dragón en el arca?")
print("🐲" in arca)  # False

#eliminar el 🦄 unicornio
arca.pop("🦄")

#modificar cantidad de 🦒 jirafa a 2
arca["🦒"] = 2

# Vaciar el arca después del diluvio
arca.clear()

#arca vacia
print("\nArca después del diluvio:")
print(arca)  # {}

