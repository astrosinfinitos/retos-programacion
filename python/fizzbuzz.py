#
# Escribe un programa que muestre por consola (con un print) los
# números de 1 a 100 (ambos incluidos y con un salto de línea entre
# cada impresión), sustituyendo los siguientes:
# - Múltiplos de 3 por la palabra "fizz".
# - Múltiplos de 5 por la palabra "buzz".
# - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
#

numero = 0

def fizzbuzz(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return "FizzBuzz"
    elif numero % 3 == 0:
        return "Fizz"
    elif numero % 5 == 0:
        return "Buzz"
    else:
        return numero
for numero in range(1,100):
    print(fizzbuzz(numero))