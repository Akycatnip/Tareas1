# Capturando excepciones
# Hasta ahora hemos visto qué es una excepción, cuándo se lanza y cómo se captura
# a través de la estructura try-except.
#
# El mismo código puede lanzar excepciones distintas.
# Al lanzarse una excepción se crea un objeto que da información de dicha excepción.
# Debemos capturarlo y hacer lo que nos convenga en cada momento.
#
# A continuación se crea una función que divide dos números. Los errores posibles son:
#
# El divisor sea cero.
# Que el dividendo o el divisor no sean números
def divide_numeros(dividendo, divisor):
    """
    Devuelve la división de dos valores

    :param dividendo: dividendo
    :param divisor: divisor
    :return: cociente de dos valores
    """
    try:
        return dividendo / divisor
    except ZeroDivisionError:
        return "Error: División por cero no permitida."
    except TypeError:
        return "Error: Ambos valores deben ser números."
    except Exception as e:
        return f"Error inesperado: {e}"
# El este caso se capturan las excepciones. La función devuelve:
#
# un número si se ha realizado la división.
# un mensaje de error si se ha capturado la excepción
# Entrega los siguientes códigos con sus respectivas pruebas.
# Usa parámetros con valores por defecto:
#
# En dame_numero.py crea una función que pida un número por teclado y lo devuelva.
# En caso de no introducir un número captura la excepción y muestra un mensaje de
# error hasta que se introduzca un número válido. Usa parámetros por defecto
def dame_numero(entero="Introduce un número: "):
    while True:
        try:
            entero_usuario = input(entero)

            if entero_usuario.isdigit():  # Comprueba si es un número positivo
                print(f"El número es {entero_usuario}")
                return int(entero_usuario)  # Ahora sí devolvemos un entero
            else:
                print(f"El valor '{entero_usuario}' no es un número entero, inténtalo de nuevo")

        except TypeError:
            print("He dicho un número")
dame_numero()
# En dame_numero_entero.py crea una función que pida un número entero
# por teclado y lo devuelva. En caso de no introducir un número entero captura
# la excepción y muestra un mensaje de error hasta que se introduzca un número entero válido.


# En dame_entero_positivo.py crea una función que pida un número entero positivo por teclado
# y lo devuelva. En caso de no introducir un número entero positivo captura la excepción
# y muestra un mensaje de error hasta que se introduzca un número entero positivo válido.



# En dame_positivo.py crea una función que pida un número positivo por teclado y lo devuelva. En caso de no introducir un número positivo captura la excepción y muestra un mensaje de error hasta que se introduzca un número positivo válido.
# En divide.pycrea una función que devuelva la división de dos valores. Lanza/captura todos los errores posibles, incluída la falta de parámetros. Usa el código que se adjunta y analiza qué ocurre al comentar los distintos bloques de except.