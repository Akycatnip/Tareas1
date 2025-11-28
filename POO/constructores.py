class A:
    def __str__(self): #no definimos init, python crea uno por defecto
        return "A"

class B:
    def __init__(self): #constructor sin parámetros
        self.mensaje = "Valor predeterminado de B"
    def __str__(self):
        return f"{self.mensaje}"

class C:
    def __init__(self,x): #constructor parametrizado 1 atributo
        self.x=x
    def __str__(self):
        return self.x

class D:
    def __init__(self,x,y):#dos atributos obligatorios
        self.x=x
        self.y=y

    def __str__(self):
        return f"{self.x} , {self.y}"

class E:
    def __init__(self, x=0, y=0):
        self.x=x#contructor con valores predeterminados
        self.y=y
    def __str__(self):
        return f"{self.x} , {self.y}"


# ----------------------------
# Clase A: Constructor por defecto (automático)
# ----------------------------
class A:
    # No definimos __init__, Python crea uno por defecto
    def __str__(self):
        return "Objeto de clase A (constructor por defecto automático)"


# ----------------------------
# Clase B: Constructor sin parámetros, inicializa atributos con valores predeterminados
# ----------------------------
class B:
    def __init__(self):
        self.mensaje = "Valor predeterminado de clase B"

    def __str__(self):
        return f"Clase B -> mensaje='{self.mensaje}'"


# ----------------------------
# Clase C: Constructor parametrizado (un solo atributo)
# ----------------------------
class C:
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return f"Clase C -> x={self.x}"


# ----------------------------
# Clase D: Constructor parametrizado (dos atributos obligatorios)
# ----------------------------
class D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Clase D -> x={self.x}, y={self.y}"


# ----------------------------
# Clase E: Constructor parametrizado con valores por defecto y parámetros con nombre
# ----------------------------
class E:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Clase E -> x={self.x}, y={self.y}"


# ----------------------------
# Pruebas de construcción de objetos
# ----------------------------

print("=== Clase A ===")
objA = A()
print(objA)

print("\n=== Clase B ===")
objB = B()
print(objB)

print("\n=== Clase C ===")
objC = C(10)  # Constructor con un parámetro
print(objC)

print("\n=== Clase D ===")
objD = D(1, 2)  # Constructor con dos parámetros obligatorios
print(objD)

print("\n=== Clase E ===")
# Diferentes formas de invocar el constructor
print(E())  # ambos valores por defecto
print(E(11))  # primer parámetro posicional
print(E(11, 22))  # ambos parámetros posicionales
print(E(x=33))  # primer parámetro con nombre
print(E(y=44))  # segundo parámetro con nombre
print(E(x=55, y=66))  # ambos parámetros con nombre
print(E(y=55, x=66))  # intercambio de parámetros por nombre
