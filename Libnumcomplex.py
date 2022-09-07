import math
from fractions import Fraction


# Autor: Juan Esteban Medina Rivas

# funciones para realizar las operaciones de números complejos

# Funciún suma: realiza sumas de números complejos
def suma(a, b):
    real = a[0] + b[0]
    img = a[1] + b[1]
    print('Suma => ' + str(real) + ' + ' + str(img) + 'i')
    return real, img


# Función resta: realiza restas de números complejos
def resta(a, b):
    real = a[0] - b[0]
    img = a[1] - b[1]
    print('Resta => ' + str(real) + ' + ' + str(img) + 'i')
    return real, img


# Función multiplicación: realiza multiplicaciones de números complejos
def multiplicacion(a, b):
    real = (a[0] * b[0]) - (a[1] * b[1])
    img = (a[0] * b[1]) + (b[0] * a[1])
    print('Multiplicación => ' + str(real) + ' + ' + str(img) + 'i')
    return real, img


# Función division: realiza divisiones de numeros complejos
def division(a, b):
    if modulo2(b[0], b[1]) == 0:
        return "Error, division por 0"
    else:
        real = (a[0] * b[0] + a[1] * b[1]) / (b[0] ** 2 + b[1] ** 2)
        img = (a[0] * b[1] + b[0] * a[1]) / (b[0] ** 2 + b[1] ** 2)
        print('División => ' + str(Fraction((a[0] * b[0] + a[1] * b[1]), (b[0] ** 2 + b[1] ** 2))) + ' + '
              + str(Fraction((a[0] * b[1] + b[0] * a[1]), (b[0] ** 2 + b[1] ** 2))))
        return real, img


# Función modulo: halla el modulo de un número complejo
def modulo(a, b):
    modul = math.sqrt(a ** 2 + b ** 2)
    print('Módulo => ' + str(round(modul, 4)))
    return modul


# Función modulo2: halla el modulo al cuadrado ( |x|^2 ) de un número complejo
def modulo2(c, d):
    modul2 = c ** 2 + d ** 2
    print('Módulo^2 => ' + str(modul2))
    return modul2


# Función conjugado: halla el conjugado de un número complejo
def conjugado(a, b):
    print('Conjugado => ' + str(a) + ' + ' + str(-b) + 'i')
    return a, -b


# Función polar: convierte de coordenadas cartesianas a polares
def polar(a, b):
    magnitud = math.sqrt((a ** 2) + (b ** 2))
    angulo = math.atan2(b, a)
    # print('Coordenadas Polares : ' + 'ρ = ' + str(round(magnitud, 4)) + '  ' + 'θ = ' + str(round(angulo, 4)))
    # Este print presenta un error desconocido hasta el momento al momento de realizar los tests
    return magnitud, angulo


# Función cartesiano: convierte de coordenadas polares a cartesianas
def cartesiano(a, b):
    x = a * math.cos(b)
    y = a * math.sin(b)
    print('Coordenadas Cartesianas => ' + str(round(x, 4)) + ' + ' + str(round(y, 4)) + 'i')
    return x, y


# Función fase: halla la fase de un número complejo
def fase(a, b):
    f = math.atan2(b, a)
    print('Fase => ' + str(round(f, 4)))
    return f


# Función printnumcomplejos: Escribe de una mejor manera el resultado de las operaciones de números complejos
# def printnumcomplejos(c):
# return print(str(c[0]) + ' + ' + str(c[1]) + 'i')


# Prueba de las diferentes funciones
# suma((1, 2), (2, 3))
# resta((1, 2), (2, 3))
# multiplicacion((1, 2), (2, 3))
# division((2, 3), (3, 5))
# modulo(5, 2)
# conjugado(5, 2)
# polar(4, 3)
# cartesiano(8.246211251235321, 1.3258176636680326)
# fase(2, 5)
