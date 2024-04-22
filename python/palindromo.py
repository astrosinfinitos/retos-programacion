#El ejercicio de hoy también es bastante sencillo, pues debemos determinar si una frase es un palindromo o no lo es
#Un palindromo es una Palabra o frase cuyas letras están dispuestas de tal manera que resulta la
#misma leída de izquierda a derecha que de derecha a izquierda;
# por ejemplo, anilina; dábale arroz a la zorra el abad.

def palindromo(palabra):
  palabra = palabra.lower()
  palindromo = palabra == palabra[::-1]
  if palindromo:
    print("La palabra " +palabra+ " es un palindromo")
  else:
    print("La palabra " +palabra+ " no es un palindromo")
  return palindromo

# Ejemplo de uso
palabra = input("Ingresa una palabra: ")
palindromo(palabra)
