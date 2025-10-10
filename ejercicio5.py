# Condicionales
#
# Crea los siguientes programas en python
# 1. "par_impar.py"Lee desde el teclado un número entero y determina si es par o impar.
numero = int(input("Dame un numero:\n"))
if numero%2==0:
    print (f"El número {numero} es par.")
else:
    print (f"El número {numero} es impar.")

# 2. "positivo_negativo_cero.py"Lee desde el teclado un número entero y determina si es positivo, negativo o cero.
numero = int(input("Dame un numero:\n"))
if numero == 0:
    print (f"El número {numero} es 0.")
else:
    if numero >0:
        print (f"El número {numero} es positivo")
    else:
        print (f"El número {numero} es negativo")

# 3. "primo_compuesto.py"Lee desde el teclado un número entero y determina si es primo o compuesto.
numero = int(input("Dame un número: \n"))
if numero <=1:
    print(f"El número {numero}no es primo")
else:
    es_primo = True
    for i in range (2, numero):
        if numero % i ==0:
            es_primo = False
            break
    if es_primo:
        print (f"El número {numero} es primo")
    else:
        print (f"El número {numero} no es primo")
# 4. "mayor_menor_edad.py"Lee desde el teclado la edad de una persona y determina si es mayor o menor de edad.

edad = int (input("Dime tu edad: \n"))
if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")
# 5. "calificacion_0_10.py"Lee desde el teclado una calificación numérica (0-10) y determina
# la calificación en (sobresaliente, notable, suficiente, insuficiente) junto con un mensaje motivacional.
nota = float (input("Dime tu nota: \n"))
if nota < 0 or nota > 10:
    print("La calificación no es correcta")
else:
    if nota >= 9:
        print ("Sobresaliente - Enhorabuena máquina!!")
    elif nota >= 7:
        print("Notable - Muy bien, sigue así!")
    elif nota >= 5:
        print("Suficiente - Por los pelos!!")
    else:
        print("Insuficiente - Venga la próxima saldrá mejor!")


# 6. "calificacion_0_100.py"Lee desde el teclado una calificación numérica (0-100)
# y determina la calificación en letra (A-F) junto con un mensaje motivacional.

nota = float (input("Dime tu nota: \n"))
if nota < 0 or nota > 100:
    print("La calificación no es correcta")
else:
    if nota >= 900:
        print ("A - Enhorabuena máquina!!")
    elif nota >= 700:
        print("B - Muy bien, sigue así!")
    elif nota >= 600:
        print("C - Por los pelos!!")
    elif nota >= 500:
        print ("D - Raspadísimo!")
    elif nota >= 300:
        print ("E - La próxima vez será...")
    else:
        print("F - No has hecho ni el huevo...")


# 7. "mes_correspondiente.py"Lee desde el teclado un número del 1 al 12 e indica el número de mes correspondiente.

i = int(input("Dime un número del 1 al 12: \n"))
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
if 1<=i<=12:
    print(f"{meses[i-1]}")


# 8. "dias_del_mes.py"Lee desde el teclado un número del 1 al 12 e indica
# el número de días del mes correspondiente.
i = int(input("Dime un número del 1 al 12: \n"))
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
dias = [31,28,31,30,31,30,31,31,30,31,30,31]
if 1<=i<=12:
    print(f"EL mes de {meses[i-1]} tiene {dias[i-1]} días")


# 12. "mayor_de_tres.py"Lee desde el teclado tres números y determina cuál es el mayor.
# mayor_de_tres.py

# Leer los tres números
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))
numero3 = float(input("Introduce el tercer número: "))

# Determinar cuál es el mayor
mayor = max(numero1, numero2, numero3)

# Mostrar el resultado
print(f"El mayor de los tres números es: {mayor}")


# 13. "rango.py"Lee desde el teclado un número
# y determina si está dentro o fuera de un rango específico (por ejemplo, 1-100).

numero = (input("Dame un número"))


if numero in range(1, 100):
    print(f"El número {numero} está dentro del rango.")
else:
    print(f"El número {numero} NO está dentro del rango.")

# 14. "vocal_consonante.py"Lee desde el teclado una letra y determina si es vocal o consonante.
letra = (input("Dame una letra"))
vocales = ["a", "e", "i", "o", "u"]
if letra in vocales:
    print("Es una vocal")
else:
    print("Es una consonante.")

# 15. "dia_semana.py"Lee desde el teclado un número del 1 al 7 e indica el día de la semana correspondiente.
# 16. "estacion_ano.py"Lee desde el teclado un mes (1-12) e indica la estación del año correspondiente.
# 17. "mayor_menor.py"Lee desde el teclado dos números y determina cuál es mayor, menor o si son iguales.
# 18. "edad_categoria.py"Lee desde el teclado la edad de una persona y determina su categoría (niño, adolescente, adulto, adulto mayor).
# 19. "calificacion_detallada.py"Lee desde el teclado una calificación numérica (0-100) y determina la calificación en letra (A-F) junto con un mensaje motivacional y la cantidad de puntos necesarios para alcanzar la siguiente calificación.


