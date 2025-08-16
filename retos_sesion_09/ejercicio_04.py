#4
#listas paralelas: productos y precios

productos = ["Chocman", "Bon Bon Bum", "Oreo", "Chizitos", "Trululu"]
precios   = [1.5,       0.8,           2.0,    1.2,        0.5]

print("Productos:", productos)
print("Precios:  ", precios)

#Agregar 2 productos nuevos al final
productos.append("Galleta Dinosaurio")
precios.append(2.3)

productos.append("Panditas")
precios.append(1.0)

print("\nDespués de agregar 2 productos:")
print("Productos:", productos)
print("Precios:  ", precios)

#eliminar "Bon Bon Bum"
i_bonbon = productos.index("Bon Bon Bum")
productos.pop(i_bonbon)
precios.pop(i_bonbon)

print("\nDespués de eliminar 'Bon Bon Bum':")
print("Productos:", productos)
print("Precios:  ", precios)

#¿cuanto cuesta "Oreo" y "Chizitos"?
i_oreo = productos.index("Oreo")
i_chiz = productos.index("Chizitos")
print("\nPrecio de Oreo:", precios[i_oreo])
print("Precio de Chizitos:", precios[i_chiz])

#cual es el producto más caro y el más barato?
i_max = precios.index(max(precios))
i_min = precios.index(min(precios))
print("\nProducto más caro:", productos[i_max], "->", precios[i_max])
print("Producto más barato:", productos[i_min], "->", precios[i_min])

# Parte 2/2

productos = ["Chocman", "Oreo", "Chizitos", "Trululu", "Galleta Dinosaurio", "Panditas"]
precios   = [1.5,       2.0,     1.2,       0.5,       2.3,                 1.0]

# cuantos productos hay?
print("\nTotal de productos:", len(productos))

#cunto cuestan todos los productos?
print("Precio total de todos los productos:", sum(precios))

#ordenar del más barato al más caro
productos_copia = productos.copy()
precios_copia   = precios.copy()
productos_orden = []
precios_orden   = []

while len(precios_copia) > 0:
    i_min = precios_copia.index(min(precios_copia))

    productos_orden.append(productos_copia.pop(i_min))
    precios_orden.append(precios_copia.pop(i_min))

print("\nProductos ordenados del más barato al más caro:")
print("Productos:", productos_orden)
print("Precios:  ", precios_orden)

#eliminar todos los productos de las listas
productos.clear()
precios.clear()
print("\nDespués de limpiar la tienda:")
print("Productos:", productos)
print("Precios:  ", precios)
