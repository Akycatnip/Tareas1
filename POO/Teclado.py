class Teclado:
    def pedir_entero(self, mensaje="Introcude un número entero:\n"):
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

