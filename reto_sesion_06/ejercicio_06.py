#ejercicio 6
numero = 300
cubo = numero * numero * numero
mayor_que_cero = cubo > 0
menor_que_limite = cubo < 27000000

dentro_del_rango = mayor_que_cero and menor_que_limite

print("ejercicio 6")
print("El cubo de", numero, "es", cubo)
print("¿Está dentro del rango?", dentro_del_rango)
