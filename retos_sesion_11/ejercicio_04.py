#hsbitats con especies en peligro
habitats = {
    "polo norte": {
        "especies": {"oso polar", "morsa", "ballena"}
    },
    "amazonas": {
        "especies": {"tigre", "mono", "guacamayo"}
    }
}

# Agregar más hábitat
habitats.update({
    "sabana africana": {
        "especies": {"león", "elefante"}
    },
    "océano pacífico": {
        "especies": {"delfín", "tiburón"}
    }
})

#verificar si existe el hábitat "amazonas"
print("¿Existe el hábitat 'amazonas'?", "amazonas" in habitats)

#añadir "anaconda" al hábitat "amazonas"
habitats["amazonas"]["especies"].add("anaconda")


print("\nHábitats en peligro y especies:")
print("Polo Norte:", habitats["polo norte"]["especies"])
print("Amazonas:", habitats["amazonas"]["especies"])
print("Sabana Africana:", habitats["sabana africana"]["especies"])
print("Océano Pacífico:", habitats["océano pacífico"]["especies"])
