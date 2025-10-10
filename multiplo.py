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


# 15. "dia_semana.py"Lee desde el teclado un número del 1 al 7 e indica el día de la semana correspondiente.
numero = int(input("Dime un número del 1 al 7\n"))
dias_semana =['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
if numero in range (1,7):
    print(f"El día número {numero} de la semana es: {dias_semana[numero - 1]}")

# 16. "estacion_ano.py"Lee desde el teclado un mes (1-12) e indica la estación del año correspondiente.
numero = int(input("Dime un número del 1 al 12\n"))
if numero in (3,4,5):
    print("Es primavera")
elif numero in (6,7,8):
    print ("Es verano")
elif numero in (9,10,11):
    print("Es otoño")
else:
    print("Es invierno")
# 17. "mayor_menor.py"Lee desde el teclado dos números y determina cuál es mayor, menor o si son iguales.
numero1 =int(input("Dime un número\n"))
numero2= int(input("Dime otro\n"))
if numero1==numero2:
    print("Son iguales")
elif numero1>numero2:
    print(f"el número {numero1} es mayor que el {numero2}")
else:
    print(f"El número {numero2} es mayor que el {numero1}")
# 18. "edad_categoria.py"Lee desde el teclado la edad de una persona y determina su categoría
# (niño, adolescente, adulto, adulto mayor).
edad= int(input("Dime tu edad\n"))
if edad in range (0,15):
    print("Eres un niño")
elif edad in range(15,18):
    print("Eres un adolescente")
elif edad in range(18,65):
    print("Eres un adulto")
else:
    print("Estás a punto de renacer")
# 19. "calificacion_detallada.py"Lee desde el teclado una calificación numérica (0-100)
# y determina la calificación en letra (A-F) junto con un mensaje motivacional
# y la cantidad de puntos necesarios para alcanzar la siguiente calificación.


