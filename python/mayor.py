#Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. 
#Es cierto que python tiene una función max() incorporada, 
#pero hacerla nosotros mismos es un muy buen ejercicio.

num1 = 4
num2 = 3

def max(num1, num2):
    if num1 > num2:
        print("El número " + str(num1) + " es mayor que " + str(num2))
    else:
        print("El número " + str(num2) + " es mayor que " + str(num1))

max(num1, num2) 