# variado.py
# Programa con múltiples opciones de manejo de arrays

import random

# -------------------------------------------------
# 1. Inversión de 10 números (range y slicing)
# -------------------------------------------------

def invertir_numeros_range():
    nums = []
    print("Introduce 10 números:")
    for _ in range(10):
        nums.append(int(input("Número: ")))
    print("Orden inverso (range):")
    for i in range(len(nums)-1, -1, -1):
        print(nums[i])

def invertir_numeros_slicing():
    nums = []
    print("Introduce 10 números:")
    for _ in range(10):
        nums.append(int(input("Número: ")))
    print("Orden inverso (slicing):")
    print(nums[::-1])

# -------------------------------------------------
# 2. Arrays secuenciados
# -------------------------------------------------

def arrays_secuenciados():
    array1 = list(range(1, 16))
    array2 = list(range(16, 31))
    array3 = list(range(31, 46))

    print("array1:", array1)
    print("array2:", array2)
    print("array3:", array3)

# -------------------------------------------------
# 3. Arrays de potencias
# -------------------------------------------------

def arrays_potencias():
    numbers = [random.randint(0, 100) for _ in range(15)]
    squares = [n*n for n in numbers]
    cubes = [n*n*n for n in numbers]

    print("Numbers \t Squares \t Cubes")
    for n, s, c in zip(numbers, squares, cubes):
        print(f"{n}\t{s}\t{c}")

# -------------------------------------------------
# 4. Max y Min etiquetado
# -------------------------------------------------

def max_min():
    nums = []
    print("Introduce 10 números:")
    for _ in range(10):
        nums.append(int(input("Número: ")))

    max_val = max(nums)
    min_val = min(nums)

    print("Resultado:")
    for n in nums:
        etiqueta = ""
        if n == max_val:
            etiqueta = " máximo"
        if n == min_val:
            etiqueta = " mínimo"
        print(n, etiqueta)

# -------------------------------------------------
# 5. Media de 10 números
# -------------------------------------------------

def media():
    nums = []
    print("Introduce 10 números:")
    for _ in range(10):
        nums.append(int(input("Número: ")))

    avg = sum(nums) / len(nums)
    print("La media es:", avg)

# -------------------------------------------------
# 6. Separar pares e impares
# -------------------------------------------------

def separar_pares_impares():
    nums = [random.randint(0, 100) for _ in range(20)]
    print("Array original:", nums)

    pares = [n for n in nums if n % 2 == 0]
    impares = [n for n in nums if n % 2 != 0]

    resultado = pares + impares
    print("Pares primero, impares después:", resultado)

# -------------------------------------------------
# 7. Desplazamiento circular a la derecha
# -------------------------------------------------

def desplazar():
    nums = []
    print("Introduce 15 números:")
    for _ in range(15):
        nums.append(int(input("Número: ")))

    ultimo = nums[-1]
    for i in range(len(nums)-1, 0, -1):
        nums[i] = nums[i-1]
    nums[0] = ultimo

    print("Array desplazado:", nums)

# -------------------------------------------------
# MENÚ PRINCIPAL
# -------------------------------------------------

def menu():
    while True:
        print("\n--- MENÚ variado.py ---")
        print("1. Invertir números (range)")
        print("2. Invertir números (slicing)")
        print("3. Arrays secuenciados")
        print("4. Arrays potencias")
        print("5. Máximo y mínimo etiquetado")
        print("6. Media de 10 números")
        print("7. Separar pares e impares")
        print("8. Desplazar array 1 posición")
        print("9. Salir")

        op = input("Elige una opción: ")

        if op == "1": invertir_numeros_range()
        elif op == "2": invertir_numeros_slicing()
        elif op == "3": arrays_secuenciados()
        elif op == "4": arrays_potencias()
        elif op == "5": max_min()
        elif op == "6": media()
        elif op == "7": separar_pares_impares()
        elif op == "8": desplazar()
        elif op == "9": break
        else: print("Opción no válida")

if __name__ == "__main__":
    menu()
