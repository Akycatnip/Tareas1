# Crea una clase Menu que gestione un menú para que el usuario elija entre varias opciones.
# El menú mostrará un título y un conjunto de opciones (incluida Salir) enumeradas del 1
# en adelante. Instancia con varios menús para hacer las pruebas.

class Menu:
    def __init__(self, titulo, opcion):
       self.opcion = opcion
       self.titulo = titulo

    def mostrar(self):
        print(f"{self.titulo}")
        for i, opcion in enumerate(self.opcion, start =1):
            print(f"{i}. {opcion}")
        return input("Elige una opción\n")



def crear_array():
    print("Creando array...")
    return []

def recorrer_array(a):
    print("Array:", a)

def buscar_elemento(a):
    print("Buscar elemento")

def insertar_elemento(a):
    print("Insertar elemento")

def eliminar_elemento(a):
    print("Eliminar elemento")

def actualizar_elemento(a):
    print("Actualizar elemento")


# Crear un menú de prueba
menu_principal = Menu("MENÚ PRINCIPAL", [
    "Crear array",
    "Recorrer array",
    "Buscar elemento",
    "Insertar elemento",
    "Eliminar elemento",
    "Actualizar elemento",
    "Salir"
])

array = []

while True:
    opcion = menu_principal.mostrar()

    if opcion == 1:
        array = crear_array()
    elif opcion == 2:
        recorrer_array(array)
    elif opcion == 3:
        buscar_elemento(array)
    elif opcion == 4:
        insertar_elemento(array)
    elif opcion == 5:
        eliminar_elemento(array)
    elif opcion == 6:
        actualizar_elemento(array)
    elif opcion == 7:
        print("Saliendo...")
        break
