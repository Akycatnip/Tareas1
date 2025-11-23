# 10. "multiplo.py"Lee desde el teclado un número y determina si es múltiplo de 3, 5 o ambos.
numero = int(input("Ingresa un numero: \n"))
if numero%3 == 0 and numero%5 == 0:
    print("El numero es múltiplo de 3 y de 5")
elif numero%3 == 0 and numero%5 != 0:
    print("El número es múltiplo de 3")
elif numero%3 != 0 and numero%5 == 0:
    print("El número es múltiplo de 5")
else:
    print("El número no es múltiplo de 3 ni de 5")