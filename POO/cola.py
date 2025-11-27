

class Cola:
    def __init__(self):
        # La cola se representará internamente como una lista
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, elemento):
        """Agrega un elemento al final de la cola."""
        self.items.append(elemento)

    def desencolar(self):
        """Elimina y devuelve el primer elemento de la cola."""
        if not self.esta_vacia():
            return self.items.pop(0)
        return "La cola está vacía"

    def frente(self):
        """Devuelve el primer elemento sin eliminarlo."""
        if not self.esta_vacia():
            return self.items[0]
        return "La cola está vacía"

    def tamaño(self):
        return len(self.items)

    def mostrar(self):
        print("Cola:", self.items)

cola = Cola()
cola.encolar(5)
cola.encolar(6)
cola.encolar(7)
cola.mostrar()

