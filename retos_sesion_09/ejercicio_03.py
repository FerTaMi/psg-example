personas = ["Iron Man", "Thanos", "Black Widow", "Loki", "Hulk", "Wanda", "Vision", "Ultron", "Spider-Man", "Doctor Strange"]

sublista = personas[5:10:2]

existe_jose = "José" in personas

# Sublista ordenada de la A a la Z
sublista_ordenada = sorted(sublista)

# Lista original ordenada de la Z a la A
personas_ordenada = sorted(personas, reverse=True)

print("Lista Marvel original:", personas)
print("Sublista [5:10:2]:", sublista)
print("¿'José' está en la lista?", existe_jose)
print("Sublista ordenada A-Z:", sublista_ordenada)
print("Lista original ordenada Z-A:", personas_ordenada)
