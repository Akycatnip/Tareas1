# Crea una clase Puerta cuyo estado sea "abierta" o "cerrada".
# Implementa los métodos abrir() y cerrar().

class Puerta:
    def __init__(self,estado="cerrada"):
        if estado not in["abierta", "cerrada"]:
            raise ValueError("La puerta puede estar abierta o cerrada")
        self.estado = estado

    def __str__(self, mensaje):
        return f"La puerta está {self.estado}"

    def abrir(self):
        if self.estado == "abierta":
            print("Puerta ya está abierta")
        else:
            self.estado = "abierta"
            print ("Puerta abierta")

    def cerrar(self):
        if self.estado == "cerrada":
            print("Puerta ya cerrada")

        else:
            self.estado = "cerrada"
            print ("Puerta cerrada")



