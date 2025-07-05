#postres favoritos de Jane y Jhon 🍰
jane = {"Lemon Pie", "Brownie", "Tarta de Manzana", "Helado de Chocolate", "Flan"}
jhon = {"Carrot Cake", "Croissant de Chocolate", "Lemon Pie", "Tarta de Manzana", "Pudding"}

# ostres que tienen en común
comunes = jane & jhon
print("🍭 Postres en común:", comunes)

#valculamos compatibilidad (basado en Jane, que tiene 5 postres)
porcentaje = (len(comunes) / len(jane)) * 100

#el resultado de compatibilidad
if porcentaje > 50:
    print(f"💖 ¡Son compatibles! Tienen un {porcentaje:.0f}% de gustos en común.")
else:
    print(f"💔 Mmm... solo un {porcentaje:.0f}% en común. Hora de charlarlo 😅.")
