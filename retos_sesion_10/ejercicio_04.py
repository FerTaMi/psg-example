#5
# Postres favoritos
jane = ["Lemon Pie", "Brownie", "Tarta de Manzana", "Helado de Chocolate", "Flan"]
jhon = ["Carrot Cake", "Croissant de Chocolate", "Lemon Pie", "Tarta de Manzana", "Pudding"]

# Buscamos postres que no tienen en común
solo_jane = []
for postre in jane:
    if postre not in jhon:
        solo_jane.append(postre)

solo_jhon = []
for postre in jhon:
    if postre not in jane:
        solo_jhon.append(postre)

#Calculamos porcentaje con el total de postres de ambos
diferentes = solo_jane + solo_jhon
total = len(jane) + len(jhon)
porcentaje = (len(diferentes) / total) * 100

print("Postres diferentes:", diferentes)
print("Porcentaje de diferencia:", porcentaje)
