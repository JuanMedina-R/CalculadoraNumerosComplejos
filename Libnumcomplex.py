import math

# funciones para realizar las diferentes operaciones de numeros complejos

# Funcion suma: realiza sumas de numeros complejos
def suma(a, b):
    real = a[0] + b[0]
    img = a[1] + b[1]
    return real, img


# Funcion resta: realiza restas de numeros complejos
def resta(a, b):
    real = a[0] - b[0]
    img = a[1] - b[1]
    return real, img


# Funcion multiplicación: realiza multiplicaciones de numeros complejos
def multiplicacion(a, b):
    real = (a[0] * b[0]) - (a[1] * b[1])
    img = (a[0] * b[1]) + (b[0] * a[1])
    return real, img


# Funcion division: realiza divisiones de numeros complejos
def division(a, b):
    if modulo2(b[0], b[1]) == 0:
        return "Error, division por 0"
    else:
        real = (a[0] * b[0] + a[1] * b[1]) / (b[0] ** 2 + b[1] ** 2)
        img = (a[0] * b[1] + b[0] * a[1]) / (b[0] ** 2 + b[1] ** 2)
        return real, img


# Funcion modulo: halla el modulo de un número complejo
def modulo(a, b):
    modulo = math.sqrt(a ** 2 + b ** 2)
    return modulo


# Funcion modulo2: halla el modulo al cuadrado ( |x|^2 ) de un número complejo
def modulo2(c, d):
    modulo2 = c ** 2 + d ** 2
    return modulo2


# Funcion conjugado: halla el conjugado de un número complejo
def conjugado(a, b):
    return a, -b


# Funcion polar: convierte de coordenadas cartesianas a polares
def polar(a, b):
    magnitud = math.sqrt((a ** 2) + (b ** 2))
    angulo = math.atan2(b, a)
    return magnitud, angulo


# Funcion cartesiano: convierte de coordenadas polares a cartesianas
def cartesiano(a, b):
    x = a * math.cos(b)
    y = a * math.sin(b)
    return x, y


# Funcion fase: halla la fase de un número complejo
def fase(a, b):
    f = math.atan2(b, a)
    return f


# Prueba de las diferentes funciones
# print(suma((1, 2), (2, 3)))
# print(resta((1, 2), (2, 3)))
# print(multiplicacion((1, 2), (2, 3)))
# print(division((2, 3), (3, 5)))
# print(modulo(5, 2))
# print(conjugado(5, 2))
# print(polar(4, 3))
# print(cartesiano(8.246211251235321, 1.3258176636680326))
# print(fase(2, 5))
