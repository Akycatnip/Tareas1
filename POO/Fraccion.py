# Crea una clase Fraccion que sume, reste, multiplique y divida dos fracciones

class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def calcular(self):
        return (self.numerador/self.denominador)

def sumar(fraccion1, fraccion2):
    return fraccion1.calcular() + fraccion2.calcular()
def resta(fraccion1, fraccion2):
    return fraccion1.calcular() - fraccion2.calcular()
def multiplicar(fraccion1, fraccion2):
    return fraccion1.calcular() * fraccion2.calcular()
def dividir(fraccion1, fraccion2):
    return fraccion1.calcular() / fraccion2.calcular()
fraccion1 = Fraccion(1, 2)
fraccion2 = Fraccion(2, 3)
print (sumar(fraccion1, fraccion2))
print (resta(fraccion1, fraccion2))
print(multiplicar(fraccion1, fraccion2))
print(dividir(fraccion1, fraccion2))
