class Carta:
    def __init__(self,palo,figura):
        self.palo = palo
        self.figura = figura

    def __str__(self):
        return f"{self.figura} de {self.palo}"

carta1 = Carta("oros","As")
carta2 = Carta("Espadas","Rey")

print(carta1)
print(carta2)


class Baraja:
    palos = ["oros", "copas", "espadas", "bastos"]
    figuras = ["as", "dos", "tres", "cuatro", "cinco", "seis", "siete",
               "sota", "caballo", "rey"]

    def __init__(self):
        self.cartas = [Carta(palo,figura)
            for palo in Baraja.palos
            for figura in Baraja.figuras]


    def mostrar(self):
        for carta in self.cartas:
            print(carta)

baraja1 = Baraja()
baraja1.mostrar()