#
# Crea un programa se encargue de transformar un número
# decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
#

def ingresar_numero():
    numero_decimal = int(input("Ingrese un número decimal: "))
    return numero_decimal

numero = ingresar_numero()
print("Número ingresado: ",numero)

def decimal_binario(numero):
    binario = ""
    while numero > 0:
        residuo = numero % 2
        binario = str(residuo) + binario
        numero = numero // 2
    print("El número en binario es: ", binario)

decimal_binario(numero)