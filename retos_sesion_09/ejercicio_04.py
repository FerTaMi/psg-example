productos = ["Chocman", "Bon Bon Bum", "Oreo", "Chizitos", "Trululu"]

precios = [1.5, 0.8, 2.0, 1.2, 0.5]

productos.append("Galleta Dinosaurio")
precios.append(2.3)

productos.append("Panditas")
precios.append(1.0)

if "Bon Bon Bum" in productos:
    index_bonbon = productos.index("Bon Bon Bum")
    productos.pop(index_bonbon)
    precios.pop(index_bonbon)

#¿Cuánto cuestan "Oreo" y "Chizitos"?
precio_oreo = precios[productos.index("Oreo")] if "Oreo" in productos else "No está"
precio_chizitos = precios[productos.index("Chizitos")] if "Chizitos" in productos else "No está"

# ¿Producto más caro y más barato?
precio_max = max(precios)
precio_min = min(precios)
producto_max = productos[precios.index(precio_max)]
producto_min = productos[precios.index(precio_min)]

print("Productos:", productos)
print("Precios:", precios)
print("Precio de Oreo:", precio_oreo)
print("Precio de Chizitos:", precio_chizitos)
print("Producto más caro:", producto_max, "->", precio_max)
print("Producto más barato:", producto_min, "->", precio_min)



productos = ["Chocman", "Oreo", "Chizitos", "Trululu", "Galleta Dinosaurio", "Panditas"]
precios = [1.5, 2.0, 1.2, 0.5, 2.3, 1.0]

total_productos = len(productos)

# ¿Cuánto cuestan todos los productos?
total_precio = sum(precios)

# Ordenar productos y precios del más barato al más caro
productos_y_precios = list(zip(productos, precios))
ordenados = sorted(productos_y_precios, key=lambda x: x[1])  # por precio

# Separar listas 
productos_ordenados = [item[0] for item in ordenados]
precios_ordenados = [item[1] for item in ordenados]

# Eliminar todos los productos de las listas
productos.clear()
precios.clear()

# Resultados
print("total de productos:", total_productos)
print("Precio total de todos los productos:", total_precio)
print("Productos ordenados del más barato al más caro:")
print("Productos:", productos_ordenados)
print("Precios:", precios_ordenados)
print("productos después de limpiar la tienda:", productos)
print("precios después de limpiar la tienda:", precios)
