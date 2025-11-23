# ---------------------------------------------
# FUNCIONES PARA OPERAR SOBRE UN ARRAY (LISTA)
# ---------------------------------------------

def crear_array():
    array = []
    n = int(input("¿Cuántos elementos deseas añadir? "))
    for i in range(n):
        elemento = input(f"Elemento {i+1}: ")
        array.append(elemento)
    print("Array creado:", array)
    return array


def recorrer_array(array):
    print("Recorriendo el array:")
    for i, elemento in enumerate(array):
        print(f"[{i}] -> {elemento}")


def buscar_elemento(array):
    objetivo = input("Elemento a buscar: ")
    if objetivo in array:
        indice = array.index(objetivo)
        print(f"Elemento encontrado en la posición {indice}")
    else:
        print("Elemento NO encontrado.")


def insertar_elemento(array):
    elemento = input("Elemento nuevo: ")
    indice = int(input("Posición donde insertar: "))
    if 0 <= indice <= len(array):
        array.insert(indice, elemento)
        print("Array actualizado:", array)
    else:
        print("Índice fuera de rango.")


def eliminar_elemento(array):
    indice = int(input("Posición a eliminar: "))
    if 0 <= indice < len(array):
        eliminado = array.pop(indice)
        print(f"Elemento '{eliminado}' eliminado.")
        print("Array actualizado:", array)
    else:
        print("Índice fuera de rango.")


def actualizar_elemento(array):
    indice = int(input("Posición a actualizar: "))
    if 0 <= indice < len(array):
        nuevo_valor = input("Nuevo valor: ")
        array[indice] = nuevo_valor
        print("Array actualizado:", array)
    else:
        print("Índice fuera de rango.")


# ---------------------------------------------
# MENÚ PRINCIPAL
# ---------------------------------------------
def menu():
    array = []  # variable LOCAL, no global

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Crear array")
        print("2. Recorrer array")
        print("3. Buscar elemento")
        print("4. Insertar elemento")
        print("5. Eliminar elemento")
        print("6. Actualizar elemento")
        print("7. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            array = crear_array()

        elif opcion == "2":
            recorrer_array(array)

        elif opcion == "3":
            buscar_elemento(array)

        elif opcion == "4":
            insertar_elemento(array)

        elif opcion == "5":
            eliminar_elemento(array)

        elif opcion == "6":
            actualizar_elemento(array)

        elif opcion == "7":
            print("Saliendo...")
            break

        else:
            print("Opción inválida. Intenta de nuevo.")


# Ejecutar menú
if __name__ == "__main__":
    menu()
