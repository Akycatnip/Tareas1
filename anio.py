# 9. "anio.py"Lee desde el teclado un año y determina si es pasado, presente o futuro.
anio= int(input("Dime un año\n"))
if anio > 2025:
    print(f"El año {anio} es futuro.")
elif anio == 2025:
    print(f"El año {anio} es presente.")
else:
    print(f"El año {anio} es pasado.")

# 11. "conversion.py"Lee desde el teclado un número y pásalo a binario, decimal y hexadecimal.


numero = int (input("Dame un numero\n"))
print(f"El número {numero} en binario es: {bin(numero)}, en decimal es: {(numero)} y en hexadecimal es: {hex(numero)}")
