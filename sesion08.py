


tupla1 = (1,2,3)
tupla2 = (3,2,1)
print (tupla1 == tupla2) # False

lista = [1, 2, 3]
lista[0] = 4  # Esto SÍ funciona

tupla = (1, 2, 3)
nueva_tupla = (4,) + tupla[1:]  # (4, 2, 3)
print(nueva_tupla)

coordenadas = (3,5)
x,y = coordenadas

def coordenadas(coordenada):
    x,y = coordenada
    x = x + 1
    y = y + 1
    return (x,y)

agenda = {('Juan','Perez'): 1234567}

tupla = (1,2.0,'hola',True)

print ("Tupla de enteros")
enteros = (1,2,3,4,5,6)
print (enteros)
print (type(enteros))

print ("Tupla de cadenas")
cadenas = ("hola", "mundo", "desde", "python")
print (cadenas)
print (type(cadenas))