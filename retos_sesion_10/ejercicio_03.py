#vlientes de cada canal
tienda_fisica = {"Ana", "Luis", "Pedro", "María", "Juan"}
tienda_online = {"Pedro", "María", "Ana", "Carlos", "Laura"}

# a. Compraron en ambos canales
ambos = tienda_fisica & tienda_online
print("🟡 Compraron en ambos canales:", ambos)

# b. Solo en tienda física
solo_fisica = tienda_fisica - tienda_online
print("🔵 Solo en tienda física:", solo_fisica)

# c. Solo online
solo_online = tienda_online - tienda_fisica
print("🟣 Solo online:", solo_online)
