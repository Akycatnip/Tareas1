class Teclado:
    def pedir_entero(self, mensaje="Introduce un número entero:\n"):
        while True:
            try:
                valor = int(input(mensaje))
                return valor
            except ValueError:
                print("Error: debes introducir un número entero.")

    def pedir_decimal(self, mensaje="Introduce un número decimal:\n"):
        while True:
            try:
                valor = float(input(mensaje))
                return valor
            except ValueError:
                print("Error: debes introducir un número decimal")

    def pedir_caracter(self, mensaje="Introduce un carácter:\n"):
        while True:
            valor = input(mensaje)
            if len(valor) == 1:
                return valor
            print("Error: Introduce un solo carácter.")

    def pedir_cadena(self, mensaje="Introduce te frase:\n"):
        valor = input(mensaje)
        return valor


teclado = Teclado()

n = teclado.pedir_entero("Dame un entero: ")
d = teclado.pedir_decimal("Dame un decimal: ")
c = teclado.pedir_caracter("Dame un carácter: ")
s = teclado.pedir_cadena("Dame una cadena: ")

print("Entero:", n)
print("Decimal:", d)
print("Carácter:", c)
print("Cadena:", s)

# Crea una clase Menu que gestione un menú para que el usuario elija entre varias opciones.
# El menú mostrará un título y un conjunto de opciones (incluida Salir) enumeradas del 1
# en adelante. Instancia con varios menús para hacer las pruebas.
# Crea una clase Dado que permita el lanzamiento de un dado. Instáncialo varias veces.
# También puedes almacenar varios dados en un array de dados, lanzarlos y mostralos todos de golpe.
# Crea una clase Fraccion que sume, reste, multiplique y divida dos fracciones
#
# Vamos a ver los diferentes tipos de constructores en Python, e implementarlos en una serie de clases,
# todas en el mismo fichero. Invocaremos los constructores de las diferentes formas posibles e
# imprimiremos los objetos para ver sus estados. Recuerda sobrescribir el metodo str() en cada clase.
# Clase A: Constructor por defecto, sin parámetros. No especificado explícitamente por el desarrollador.
# Automáticamente creado por Python.
# Clase B: Constructor sin parámetros (no parametrizado). Siempre inicializa los atributos con valores predeterminados.
# Clase C: Constructor parametrizado. Inicializa un único atributo con valor proporcionado como argumento.
# Clase D: Constructor parametrizado. Inicializa dos atributos con valor proporcionado como argumentos
# posicionales/obligatorios.
# Clase E: Constructor parametrizado. Con 2 parámetros con valores predeterminados/con nombre.
# Invoca el constructor de todas las formas posibles: E(), E(11), E(11, 22), E(x=33), E(y=44), E(x=55, y=66), E(y=55, x=66)
# Crea una clase Vector que almacene un array de números. Podrá sumar y restar dos vectores
# del mismo tamaño. En caso de no coincidir debe devolver un mensaje de error. Muestra sólo
# dos decimales de cada número.
# Crea una clase Puerta cuyo estado sea "abierta" o "cerrada". Implementa los métodos abrir() y cerrar().
# Crea una clase Ascensor que simule la subida y bajada de un ascensor. Implementa los métodos viajar_a(planta_destino),
# subir(), bajar(). Ls puerta forma parte del Ascensor. El resultado de la ejecución ha de ser similar a este:

