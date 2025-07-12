
alimentos = {
    "carne": ["gato", "perro"],
    "zanahoria": ["conejo"]
}

# 4 alimentos 
alimentos.update(
    pescado=["gato", "perro"],
    semillas=["loro", "hamster"],
    avena=["conejo", "hamster"],
    pienso=["gato", "perro", "conejo"]
)

# si existe 'trigo' 
existe_trigo = "trigo" in alimentos
print("¿Existe 'trigo' en alimentos?", existe_trigo)

# Eliminar'zanahoria
del alimentos["zanahoria"]

# Mostrar el diccionario 
print("\nDiccionario de alimentos actualizado:")
print(alimentos)
