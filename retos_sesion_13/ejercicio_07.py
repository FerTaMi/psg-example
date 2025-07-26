#Crear una serie de números del 1 al 100, si el número es divisible entre 5 imprimir Fizz, si el número es divisible entre 7 imprimir Buzz, si el número es divisible entre 5 y 7 imprimir FizzBuzz


for numero in range(1, 101):
    if numero % 5 == 0 and numero % 7 == 0:
        print("FizzBuzz")
    elif numero % 5 == 0:
        print("Fizz")
    elif numero % 7 == 0:
        print("Buzz")
    else:
        print(numero)
