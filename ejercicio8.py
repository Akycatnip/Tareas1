# # Crea una lista con diferentes tipos de datos literales.
# # Recorre la lista y mediante la función type()
# # muestra el tipo de dato de cada elemento.
# # Aparece la palabra 'class' en la salida de type()
# # porque todo en Python es un objeto, y cada tipo de dato es una clase.
# # Usa el slicing para mostrar solo el nombre del tipo de dato
# # sin la palabra 'class' y sin los símbolos <>, y sin comillas.
# # Por ejemplo, para un elemento 11, la salida debería ser
# # Elemento: 11, Tipo: int.
# lista=[11,34,"pepito","Nero",-8678]
# for elemento in lista:
#     tipo = str(type(elemento))[8: -2]
#     print(f"{elemento} es tipo {tipo}")
#
#
#
# # Crea una lista de elementos falsy y otra de elementos truthy.
# # Recorre ambas listas e imprime si cada elemento es falsy o truthy.
#
# # Lista de elementos falsy
# falsy = [0, 0.0, "", [], (), {}, set(), None, False]
#
# # Lista de elementos truthy
# truthy = [1, -5, 3.14, "Hola", [1, 2], (3,), {"a": 1}, {7}, True]
#
# # Recorremos la lista falsy
# for elemento in falsy:
#     print(f"Elemento: {elemento}, Valor lógico: falsy")
#
# # Recorremos la lista truthy
# for elemento in truthy:
#     print(f"Elemento: {elemento}, Valor lógico: truthy")
#
#

# Escribe un programa que pida al usuario un número en binario (0b1010).
# Deberá convertirlo a entero en base 10, a hexadecimal (base 16) y
# a texto, mostrando los resultados.

# Escribe un programa que pida al usuario un número en octal (0o12).
# Deberá convertirlo a entero en base 10, a binario (base 2),
# a hexadecimal (base 16) y a texto, mostrando los resultados.



# Escribe un programa que pida al usuario un número en decimal (12).
# Deberá convertirlo a binario (base 2), a octal (base 8),
# a hexadecimal (base 16) y a texto, mostrando los resultados.



# # Escribe un programa que pida al usuario un número en hexadecimal
# (0x1A). Deberá convertirlo a entero en base 10, a binario (base 2)
# , a octal (base 8) y a texto, mostrando los resultados.
# Primero necesitas instalar la librería num2words
# pip install num2words

from num2words import num2words

# --- Conversión desde BINARIO ---
binario = input("Introduce un número en binario (ejemplo: 0b1010): ")
entero = int(binario, 0)
print("\n--- Conversión desde BINARIO ---")
print(f"Entero (base 10): {entero}")
print(f"Hexadecimal (base 16): {hex(entero)}")
print(f"Número en palabras: {num2words(entero, lang='es')}")

# --- Conversión desde OCTAL ---
octal = input("\nIntroduce un número en octal (ejemplo: 0o12): ")
entero = int(octal, 0)
print("\n--- Conversión desde OCTAL ---")
print(f"Entero (base 10): {entero}")
print(f"Binario (base 2): {bin(entero)}")
print(f"Hexadecimal (base 16): {hex(entero)}")
print(f"Número en palabras: {num2words(entero, lang='es')}")

# --- Conversión desde DECIMAL ---
decimal = int(input("\nIntroduce un número en decimal (ejemplo: 12): "))
print("\n--- Conversión desde DECIMAL ---")
print(f"Binario (base 2): {bin(decimal)}")
print(f"Octal (base 8): {oct(decimal)}")
print(f"Hexadecimal (base 16): {hex(decimal)}")
print(f"Número en palabras: {num2words(decimal, lang='es')}")

# --- Conversión desde HEXADECIMAL ---
hexa = input("\nIntroduce un número en hexadecimal (ejemplo: 0x1A): ")
entero = int(hexa, 0)
print("\n--- Conversión desde HEXADECIMAL ---")
print(f"Entero (base 10): {entero}")
print(f"Binario (base 2): {bin(entero)}")
print(f"Octal (base 8): {oct(entero)}")
print(f"Número en palabras: {num2words(entero, lang='es')}")
