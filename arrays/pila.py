#  Una pila es una estructura de datos que sigue el principio LIFO (Last In, First Out),
#  lo que significa que el último elemento agregado es el primero en ser removido.
# Debes pensar en una pila de platos: el último plato que colocas en la pila es el primero que quitas cuando necesitas uno.
# Mediante arrays unidimensionales, podemos implementar una pila utilizando una lista en Python:
#
# Añade al final de pila.py un menú que permita al usuario elegir entre las diferentes operaciones que se pueden
# realizar con un array unidimensional: creación, recorrido, búsqueda, inserción, eliminación y actualización.
# Crea tantas funciones como operaciones haya en el menú. Refactoriza para que todas las variables
# sean locales a las funciones.

# Definición de la clase Pila
pila = []
# Función para agregar un elemento a la pila
def push(elemento):
    pila.append(elemento)
    
# Función para remover y retornar el elemento superior de la pila
def pop():
    if not is_empty():
        return pila.pop()
    else:
        return "La pila está vacía"
# Función para verificar si la pila está vacía
def is_empty():
    return len(pila) == 0

# Función para ver el elemento superior de la pila sin removerlo
def peek():
    if not is_empty():
        return pila[-1]
    else:
        return "La pila está vacía"
while True:
    print("Menu:")
    print ("1. Agregar elemento a la pila")
    print("2. Quitar el elemento superior de la pila")
    print("3. Verificar si la pila está vacía")
    print("4. Ver el elemento superior de la pila")
    print("5. Salir")

    opcion = input("Por favor selecciona una opción del Menú:\n")

    if opcion == '1':
        elemento = input("Dime lo que quieres añadir a la lista\n")
        push(elemento)
        print(f"El elemento{elemento} ha sido añadido a la lista: {pila}")

    if opcion =='2':
        pop()
        print(f"El último elemento ha sido eliminado de la lista: {pila}")

    if opcion =='3':
        is_empty()
        print(f"La lista tiene {len(pila)} elementos.")

    if opcion =='4':
        peek()
        print(f"El último elemento de la lista es: {pila[-1]}")

    if opcion == '5':
        break






 

