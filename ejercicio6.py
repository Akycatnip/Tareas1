# Diseña estos programas siempre dentro de un bucle. Implementa al menos
# una versión con while y otra con for:
#
# Solicita por teclado un entero. Se saldrá cuando el número sea cero
numero = int(input("Introduce un numero: "))
while numero != 0:
    print("Intentalo otra vez")
    numero = int(input("Introduce un numero: "))
# Solicita por teclado una letra. Se saldrá cuando la letra sea una vocal

letra = input("Introduce una letra: ")
vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

# Comprobamos si la letra está en la lista de vocales
while letra not in vocales:
    print("Intentalo de nuevo.")
    letra = input("Introduce una letra: ")

# Si la letra es una vocal, el bucle termina
print("Es una vocal.")

# Solicita por teclado una frase. La mostrará en mayúsculas cuando la palabra contenga números

frase = input("Dime una frase")
if any(caracter.isdigit() for caracter in frase):
    print(frase.upper())

# Solicita un entero. Muestra su tabla de multiplicar.

numero = int(input("Introduce un numero: "))
for i in range(1,11):
    print(numero*i)

