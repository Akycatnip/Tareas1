class Vector:
    def __init__(self, numeros):
        self.numeros = numeros

    def __str__(self):
        numeros_formateados = [f"{num:.2f}" for num in self.numeros]
        return "[" + ",".join(numeros_formateados) + "]"
    def sumar(self, otro):
        if len(self.numeros) != len(otro.numeros):
            return "Error: los vectores no tienen el mismo tamaño"
        resultado = [a+b for a,b in zip(self.numeros, otro.numeros)]
        return Vector(resultado)
    def restar(self,otro):
        if len(self.numeros) != len(otro.numeros):
            return "Error: los vectores no tienen el mismo tamaño"
        resultado = [a-b for a,b in zip(self.numeros, otro.numeros)]
        return Vector(resultado)
# Crear vectores
v1 = Vector([1.234, 2.345, 3.456])
v2 = Vector([0.123, 1.111, 2.222])

print("Vector 1:", v1)
print("Vector 2:", v2)

# Sumar vectores
v_sum = v1.sumar(v2)
print("Suma:", v_sum)

# Restar vectores
v_res = v1.restar(v2)
print("Resta:", v_res)

# Vectores de distinto tamaño
v3 = Vector([1, 2])
print("Suma con vector distinto tamaño:", v1.sumar(v3))
