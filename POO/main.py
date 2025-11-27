from Figura import Circulo, Cuadrado, Rectangulo
from cola import Cola


class Main:
    circulo = Circulo(5)
    cuadrado = Cuadrado(5,5)
    rectangulo = Rectangulo(5,8)
    print (f"{circulo.area()}, {circulo.perimetro()}")
    print (f"{cuadrado.area()}, {cuadrado.perimetro()}")
    print (f"{rectangulo.area()}, {rectangulo.perimetro()}")



if __name__ == "__main__":
    Main()