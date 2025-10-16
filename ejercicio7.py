# # Crea los siguientes programas usando bucles for o while.
# #
# # "adivinalo.py" Genera un número aleatorio del 1 al 100. Pide al usuario que
# # lo adivine, indicando si es mayor o menor.
# # En caso de adivinarlo se sale con "EUREKA. Lo has adivinado
#
# import random
#
# # Generar número aleatorio del 1 al 100
# numero = random.randint(1, 100)
#
# print("Adivina el número del 1 al 100")
#
# # Bucle hasta que el usuario adivine
# while True:
#     try:
#         numeroUser = int(input("Dame un número: "))
#
#         if numeroUser < numero:
#             print("El número es mayor.")
#         elif numeroUser > numero:
#             print("El número es menor.")
#         else:
#             print("EUREKA. ¡Lo has adivinado!")
#             break
#     except ValueError:
#         print("Por favor, introduce un número válido.")
#
# # "adivinalo2.py" Igual que el anterior pero con un máximo de 10
# # intentos, indicando los intentos que quedan y en cuánto lo ha adivinado.
# import random
#
# # Número aleatorio entre 1 y 100
# numero_secreto = random.randint(1, 100)
# max_intentos = 10  # Puedes cambiar este número si quieres
# intentos = 0
#
# print("Adivina el número del 1 al 100")
# print(f"Tienes un máximo de {max_intentos} intentos.")
#
# # Bucle de juego
# while intentos < max_intentos:
#     try:
#         numero_usuario = int(input("Dame un número: "))
#         intentos += 1
#
#         if numero_usuario < numero_secreto:
#             print("El número es mayor.")
#         elif numero_usuario > numero_secreto:
#             print("El número es menor.")
#         else:
#             print(f"EUREKA. ¡Lo has adivinado en {intentos} intento(s)!")
#             break
#     except ValueError:
#         print("Por favor, introduce un número válido.")
# else:
#     print(f"Lo siento, has agotado tus {max_intentos} intentos. El número era {numero_secreto}.")


# "cuenta_cuentos.py" Pide un número y cuenta desde 1 hasta ese número.
numero = int(input("Dime un número del 1 al 50\n"))
i=0
while i < numero:
    print(i+1)
    i = i + 1

# "suma_numeros.py" Pide el número de iteraciones.
# En cada iteración pide un número y al final muestra la suma de los números
# positivos, la suma de los negativos y cuántos ceros se han introducido.

# Pedir al usuario cuántas iteraciones quiere hacer
iteraciones = int(input("Dime el número de iteraciones: "))

# Inicializar acumuladores
suma_positivos = 0
suma_negativos = 0
contador_ceros = 0

# Bucle para pedir números
for i in range(iteraciones):
    numero = int(input(f"Dame el número {i + 1}: "))

    if numero > 0:
        suma_positivos += numero
    elif numero < 0:
        suma_negativos += numero
    else:
        contador_ceros += 1

# Mostrar resultados
print("\n--- Resultados ---")
print(f"Suma de números positivos: {suma_positivos}")
print(f"Suma de números negativos: {suma_negativos}")
print(f"Cantidad de ceros introducidos: {contador_ceros}")


# "contador_numeros.py" Realizar un algoritmo que pida números
# (se pedirá por teclado la cantidad de números a introducir).
# El programa debe informar de cuantos números introducidos son
# mayores que 0, menores que 0 e iguales a 0.

vueltas = int(input("Dime la cantidad de números:\n/"))
mayores = 0
menores = 0
iguales = 0

for i in range(vueltas):
    numeros = float(input(f"Introduce el número {i + 1}: "))
    if numeros > 0:
        mayores+=1
    elif numeros < 0:
        menores+=1
    else:
        iguales+=1
print(f"Hay {mayores} números mayores que 0, {menores} números menores a 0 y {iguales} ceros")


# "tabla_multiplicar.py" Pide un número y muestra su tabla de multiplicar.
multiplicador= int(input("Dame un número:\n"))
for i in range(1,11):
    print(f"{multiplicador} x {i}= {multiplicador*i}")


# "factorial.py" Pide un número y muestra su factorial.
n = int(input("Dime el número:\n"))
factorial =1
for i in range(1, n+1):
    factorial *= i
print(f"El factorial de {n} es {factorial}")


# "con_caracter.py" Pide un caracter al usuario.
# Indicará si es o no vocal. Finaliza con la introducción de un "*".
caracter = input("Dame una caracter:\n")
vocales =["a","e","i","o","u","A","E","I","O","U"]
if caracter in vocales:
    print(f"La letra {caracter} es vocal")
else:
    print(f"La letra {caracter} es una consonante")


# "pares.py" Imprime todos los números pares entre
# dos números que se le pidan al usuario.
numero1=input("Dime el primer número\n")
numero2=input("Dame el segundo número\n")




# "intervalo.py" Se le pide al usuario que introduzca el limite inferior
# y superior de un intervalo.
# Si el límite inferior es mayor que el superior lo tiene que volver a pedir.
# A continuación se van introduciendo números hasta que introduzcamos el 0.
# Entonces el programa dará las siguientes informaciones:
# La suma de los números que están dentro del intervalo (intervalo abierto).
# Cuántos números están fuera del intervalo.
# Informa si hemos introducido algún número igual a los límites del intervalo.

intervalo1 = int(input("Dime el límite inferior del intervalo\n"))
intervalo2 = int(input("Dime el límite superior del intervalo\n"))
if intervalo2 > intervalo1:
    intervalo2= int(input("Vuelve a introducir el límite superior del intervalo\n"))
lista_numeros=[""]

print("Introduce todos los número que quieras y como último el 0\n")
while True:





# "potencia_sin.py" Pide dos números, uno real (base) y un entero positivo
# (exponente). Sacará por pantalla el resultado de la potencia sin utilizar
# el operador de potencia.


# "pagos.py" Una persona adquirió un producto para pagar en 20 meses.
# El primer mes pagó 10 €, el segundo 20 €, el tercero 40 € y así sucesivamente.
# Realizar un programa para determinar cuánto debe pagar mensualmente y el total
# de lo que pagará después de los 20 meses.


# "cronometro.py" Muestra un cronómetro, indicando las horas, minutos y segundos.
# Usa del módulo time time.sleep(1) para que el programa espere un segundo entre
# cada actualización.



# "primos.py" Muestra los N primeros números primos.
# Se pide por teclado la cantidad de números primos que queremos mostrar.



# "caracter_en_cadena.py" Pide una cadena y un carácter por teclado
# y muestra cuantas veces aparece el carácter en la cadena.



# "reemplazar_caracter.py" Pide una cadena y dos caracteres por teclado
# (valida que sea un carácter), sustituye la aparición del primer
# carácter en la cadena por el segundo carácter.



# "contar_palabras.py" Pide una cadena por teclado y cuenta cuántas palabras tiene.



# "mayusculas_minusculas.py" Realizar un programa que lea una cadena
# por teclado y convierta las mayúsculas a minúsculas y viceversa.



# "subcadena.py" Realizar un programa que compruebe si una
# cadena contiene una subcadena. Las dos cadenas se introducen por teclado.



# "palindromo.py" Introducir una cadena de caracteres e indicar
# si es un palíndromo. Una palabra palíndroma es aquella que
# se lee igual adelante que atrás.



# "numeros_primos.py" Lee un número por teclado e indica si
# es un número primo o no.

# "reemplazar_caracter.py" Pide una cadena y dos caracteres por
# teclado (valida que sea un carácter), sustituye la aparición
# del primer carácter en la cadena por el segundo carácter.