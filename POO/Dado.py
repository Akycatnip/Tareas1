import random

class Dado:
    def __init__(self, caras=6):
        self.caras = caras
        self.valor =None #guarda el último lanzamiento

    def lanzar(self):
        self.valor = random.randint(1,self.caras)
        return self.valor

    def __str__(self):
        return f"Dado({self.caras} caras) -> {self.valor if self.valor else '-'}"

dados = [Dado(6), Dado(6), Dado(6)]
for dado in dados:
    dado.lanzar()
for i, dado in enumerate(dados, start=1):
    print(f"Dado{i}: {dado}")