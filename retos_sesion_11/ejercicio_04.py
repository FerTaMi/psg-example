# Diccionario de hábitats con especies en peligro
habitats = {
    "polo norte": {
        "especies": {"oso polar", "morsa", "ballena"}
    },
    "amazonas": {
        "especies": {"tigre", "mono", "guacamayo"}
    }
}

# Mostrar la información de los hábitats
print("Hábitats en peligro y especies:")
for zona, datos in habitats.items():
    print(f"- {zona.title()}: {', '.join(datos['especies'])}")

# base de hábitats
habitats = {
    "polo norte" : {
        "especies": {"oso polar", "morsa", "ballena"}
    },
    "amazonas" : {
        "especies": {"tigre", "mono", "guacamayo"}
    }
}

# 2 hábitats
habitats.update({
    "sabana africana": {
        "especies": {"león", "elefante"}
    },
    "océano pacífico": {
        "especies": {"delfín", "tiburón"}
    }
})

#Existe el hábitat "amazonas"?
print("amazonas" in habitats)  # True

#Añadir "anaconda" al hábitat "amazonas"
habitats["amazonas"]["especies"].add("anaconda")


print("\nHábitats actualizados:")
for zona, datos in habitats.items():
    print(f"- {zona.title()}: {', '.join(datos['especies'])}")
