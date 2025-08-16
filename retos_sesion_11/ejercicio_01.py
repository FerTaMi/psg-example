
animal = {
    "especie": "Pulpo",
    "hábitat": "Océano Pacífico",
    "dieta": "Crustáceos y peces pequeños",
    "estado_de_salud": "Saludable",
    "edad": 4,
    "cuidadores": {"Lucía", "Carlos", "Mateo"}
}

#información del animal
print("Información del animal marino:")
for clave, valor in animal.items():
    print(f"{clave}: {valor}")



