# ---------------------------------------------------
# FUNCIONES PARA OPERAR CON UNA COLA (FIFO)
# ---------------------------------------------------

def crear_cola():
    cola = []
    n = int(input("¿Cuántos elementos deseas añadir a la cola? "))
    for i in range(n):
        elemento = input(f"Elemento {i+1}: ")
        cola.append(elemento)
    print("Cola creada:", cola)
    return cola


def recorrer_cola(cola):
    print("Recorriendo la cola:")
    for i, elemento in enumerate(cola):
        print(f"[{i}] -> {elemento}")


def buscar_elemento(cola):
    objetivo = input("Elemento a buscar: ")
    if objetivo in cola:
        indice = cola.index(objetivo)
        print(f"Elemento encontrado en la posición {indice}")
    else:
        print("Elemento NO encontrado.")


def enqueue(cola):
    elemento = input("Elemento a añadir (enqueue): ")
    cola.append(elemento)
    print("Elemento añadido al final de la cola.")
    print("Cola actualizada:", cola)


def dequeue(cola):
    if len(cola) == 0:
        print("La cola está vacía. No se puede eliminar.")
    else:
        eliminado = cola.pop(0)
        print(f"Elemento '{eliminado}' eliminado del principio de la cola (dequeue).")
        print("Cola actualizada:", cola)


def actualizar_elemento(cola):
    indice = int(input("Posición del elemento a actualizar: "))
    if 0 <= indice < len(cola):
        nuevo = input("Nuevo valor: ")
        cola[indice] = nuevo
        print("Elemento actualizado.")
        print("Cola actualizada:", cola)
    else:
        print("Índice fuera de rango.")


# ---------------------------------------------------
# MENÚ PRINCIPAL
# ---------------------------------------------------

def menu():
    cola = []  # Variable local, no global

    while True:
        print("\n--- MENÚ DE COLA (FIFO) ---")
        print("1. Crear cola")
        print("2. Recorrer cola")
        print("3. Buscar elemento")
        print("4. Insertar elemento (enqueue)")
        print("5. Eliminar elemento (dequeue")
        print("6. Actualizar elemento")
        print("7. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            cola = crear_cola()

        elif opcion == "2":
            recorrer_cola(cola)

        elif opcion == "3":
            buscar_elemento(cola)
        elif opcion == "4":
            enqueue(cola)

        elif opcion == "5":
            dequeue(cola)

        elif opcion == "6":
            actualizar_elemento(cola)

        elif opcion == "7":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intenta de nuevo.")


# Ejecutar menú solo si el archivo se ejecuta directamente
if __name__ == "__main__":
    menu()

