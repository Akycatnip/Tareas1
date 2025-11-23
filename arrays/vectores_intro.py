# -------------------------------------------------
# Función principal solicitada con todas las sentencias
# -------------------------------------------------

def main():
    # 1. Mostrar el valor del elemento 6 de un vector array_inicio
    array_inicio = [10, 20, 30, 40, 50, 60, 70]  # ejemplo con más de 6 elementos
    print("1) Elemento 6 de array_inicio:", array_inicio[5])  # índice 5 es el sexto elemento

    # 2. Inicializar los 5 primeros elementos de un array a 8
    array_ochosssss = [0] * 10  # vector de ejemplo
    for i in range(5):
        array_ochosssss[i] = 8
    print("2) array_ochosssss inicializado:", array_ochosssss)

    # 3. Calcular y mostrar el total de 100 elementos de punto flotante
    array_decimales = [i * 0.5 for i in range(100)]  # ejemplo
    total = sum(array_decimales)
    print("3) Total de array_decimales:", total)

    # 4. Copiar los 11 elementos de un array origen en el destino de 34 elementos
    array_origen = list(range(11))
    array_destino = [0] * 34

    for i in range(11):
        array_destino[i] = array_origen[i]

    print("4) array_destino tras copia:", array_destino)

    # 5. Calcular y mostrar el mayor y menor de un array de 99 elementos float
    array_decimales_casi100 = [i * 1.1 for i in range(99)]  # ejemplo

    mayor = max(array_decimales_casi100)
    menor = min(array_decimales_casi100)

    print("5) Mayor:", mayor)
    print("   Menor:", menor)


if __name__ == "__main__":
    main()
