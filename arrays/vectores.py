def demo_arrays():
    # Los arrays unidimensionales son útiles para almacenar secuencias de datos, como listas de números, cadenas, etc.
    # Para acceder a los elementos de un array, se utiliza la notación de corchetes con el índice del elemento deseado.
    # Ejemplo: array[0] accede al primer elemento del array.
    # para acceder al último elemento de un array se puede usar el índice -1.
    # Mediante la longitud del array, se puede acceder al último elemento con array[len(array) - 1].

    # creación de varios arrays unidimensionales de distintas formas:

    array1 = [10, 20, 30, 40, 50]  # Usando una lista
    array2 = list((1, 2, 3, 4, 5))  # Usando la función list()
    array3 = [i for i in range(5)]  # Usando una comprensión de listas
    array4 = []  # Creando un array vacío y luego agregando elementos
    array5 = [7] * 5  # Creando un array con valores repetidos

    # Acceso a elementos de los arrays mediante índices y corchetes
    primer_elemento_array1 = array1[0]  # Accediendo al primer elemento mediante índices
    ultimo_elemento_array2 = array2[-1]  # Accediendo al último elemento mediante índices negativos
    ultimo_elemento_array3 = array3[len(array3) - 1]  # Accediendo al último elemento mediante la longitud del array
    print("Primer elemento de array1:", primer_elemento_array1)
    print("Último elemento de array2:", ultimo_elemento_array2)
    print("Último elemento de array3:", ultimo_elemento_array3)

    # Imprimiendo los arrays para verificar su contenido
    print("Contenido de array1:", array1)
    print("Contenido de array2:", array2)
    print("Contenido de array3:", array3)
    print("Contenido de array4:", array4)
    print("Contenido de array5:", array5)

    # Agregando elementos al array4
    array4.append(100)
    array4.append(200)
    print("Contenido de array4 después de agregar elementos:", array4)
    # Modificando elementos en array1
    array1[2] = 35  # Cambiando el tercer elemento de array1
    print("Contenido de array1 después de modificar un elemento:", array1)
    # Eliminando un elemento de array2
    del array2[1]  # Eliminando el segundo elemento de array2
    print("Contenido de array2 después de eliminar un elemento:", array2)
    # Obteniendo la longitud de los arrays
    print("Longitud de array1:", len(array1))
    print("Longitud de array2:", len(array2))
    print("Longitud de array3:", len(array3))
    print("Longitud de array4:", len(array4))
    print("Longitud de array5:", len(array5))
    # Iterando sobre los elementos de array5
    print("Elementos de array5:")
    for elemento in array5:
        print(elemento)

    # Iterando mediante índices
    print("Elementos de array1 mediante índices:")
    for i in range(len(array1)):
        print(array1[i])

    # iterando con enumerate para obtener índice y valor
    print("Elementos de array3 con índices:")
    for index, value in enumerate(array3):
        print(f"Índice {index}: Valor {value}")

    # enumerate es una función (clase) incorporada en Python que permite iterar sobre una secuencia (como una lista o un array)
    # y obtener tanto el índice como el valor de cada elemento durante la iteración.
    for index, value in enumerate(array1):
        print(f"Índice {index}: Valor {value}")
    # Los arrays unidimensionales son fundamentales en la programación y se utilizan en una amplia variedad de aplicaciones,
    # desde el almacenamiento de datos hasta la manipulación de secuencias y la realización de cálculos.
    # Pueden ser manipulados fácilmente mediante operaciones como agregar, eliminar, modificar y recorrer elementos.

    # Añadiendo más elementos a array4 para demostrar su uso
    array4.extend([300, 400, 500])
    print("Contenido final de array4 después de agregar más elementos:", array4)
    # append agrega un solo elemento, mientras que extend agrega múltiples elementos de una lista u otra colección.
    array5.append(70)
    print("Contenido final de array5 después de agregar un elemento:", array5)


# Un array es una estructura de datos que almacena una colección de elementos del mismo tipo.
# En Python, los arrays unidimensionales pueden ser representados utilizando listas o la biblioteca NumPy.
# Los índices en los arrays comienzan en 0.
demo_arrays()

