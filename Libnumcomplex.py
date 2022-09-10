import math
import numpy as np
from fractions import Fraction


# Autor: Juan Esteban Medina Rivas

# Funciones para realizar operaciones de números complejos

# Funciún suma: realiza sumas de números complejos


def suma(a, b):
    real = a[0] + b[0]
    img = a[1] + b[1]
    # print('Suma => ' + str(real) + ' + ' + str(img) + 'i')
    return real, img


def inverso(a):
    real = -1 * (a[0])
    img = -1 * (a[1])
    return real, img


# Función resta: realiza restas de números complejos
def resta(a, b):
    real = a[0] - b[0]
    img = a[1] - b[1]
    # print('Resta => ' + str(real) + ' + ' + str(img) + 'i')
    return real, img


# Función multiplicación: realiza multiplicaciones de números complejos
def multiplicacion(a, b):
    real = (a[0] * b[0]) - (a[1] * b[1])
    img = (a[0] * b[1]) + (b[0] * a[1])
    # print('Multiplicación => ' + str(real) + ' + ' + str(img) + 'i')
    return real, img


# Función division: realiza divisiones de numeros complejos
def division(a, b):
    if modulo2(b[0], b[1]) == 0:
        return "Error, division por 0"
    else:
        real = (a[0] * b[0] + a[1] * b[1]) / (b[0] ** 2 + b[1] ** 2)
        img = (a[0] * b[1] + b[0] * a[1]) / (b[0] ** 2 + b[1] ** 2)
        # print('División => ' + str(Fraction((a[0] * b[0] + a[1] * b[1]), (b[0] ** 2 + b[1] ** 2))) + ' + '
        #       + str(Fraction((a[0] * b[1] + b[0] * a[1]), (b[0] ** 2 + b[1] ** 2))))
        return real, img


# Función modulo: halla el modulo de un número complejo
def modulo(a, b):
    modul = math.sqrt(a ** 2 + b ** 2)
    # print('Módulo => ' + str(round(modul, 4)))
    return modul


# Función modulo2: halla el modulo al cuadrado ( |x|^2 ) de un número complejo
def modulo2(c, d):
    modul2 = c ** 2 + d ** 2
    # print('Módulo^2 => ' + str(modul2))
    return modul2


# Función conjugado: halla el conjugado de un número complejo
def conjugado(a):
    real = a[0]
    img = -1 * (a[1])
    # print('Conjugado => ' + str(a) + ' + ' + str(-b) + 'i')
    return real, img


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
    # print('Coordenadas Cartesianas => ' + str(round(x, 4)) + ' + ' + str(round(y, 4)) + 'i')
    return x, y


# Función fase: halla la fase de un número complejo
def fase(a, b):
    f = math.atan2(b, a)
    # print('Fase => ' + str(round(f, 4)))
    return f


# Función SumaVectores: realiza la suma de dos vectores
def sumavectores(a, b):
    if len(a) == len(b):
        vector = [[0 for i in range(1)] for j in range(len(a))]
        for i in range(len(a)):
            vector[i] = suma(a[i], b[i])
        return vector
    else:
        print("Debido a que los vectores no tienen el mismo tamaño, no es posible realizar la operación")


def restavectores(a, b):
    if len(a) == len(b):
        vector = [[0 for i in range(1)] for j in range(len(a))]
        for i in range(len(a)):
            vector[i] = resta(a[i], b[i])
        return vector
    else:
        print("Debido a que los vectores no tienen el mismo tamaño, no es posible realizar la operación")


def inversovector(a):
    vector = [[0 for i in range(1)] for j in range(len(a))]
    for i in range(len(a)):
        vector[i] = inverso(a[i])
    return vector


def multescalarvector(c, a):
    vector = [[0 for i in range(1)] for j in range(len(a))]
    for i in range(len(a)):
        vector[i] = multiplicacion(c, a[i])
    return vector


def sumamatrices(a, b):
    if len(a) == len(b) and len(a[0]) == len(b[0]):
        matriz = [[0 for i in range(len(b[0]))] for j in range(len(a))]
        for i in range(len(a)):
            for j in range(len(b[0])):
                matriz[i][j] = suma(a[i][j], b[i][j])
        return matriz
    else:
        print("Debido a que las matrices no tienen tamaños compatibles, no es posible realizar la operación")


def inversomatriz(a):
    matriz = [[0 for i in range(len(a[0]))] for j in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            matriz[i][j] = inverso(a[i][j])
    return matriz


def multescalarmatriz(c, a):
    matriz = [[0 for i in range(len(a[0]))] for j in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            matriz[i][j] = multiplicacion(c, a[i][j])
    return matriz


def traspuesta(a):
    matriz = [[0 for i in range(len(a[0]))] for j in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            matriz[i][j] = a[j][i]
    return matriz


def conjugadomatriz(a):
    matriz = [[0 for i in range(len(a[0]))] for j in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            matriz[i][j] = conjugado(a[i][j])
    return matriz


def adjuntamatriz(a):
    matriz = conjugadomatriz(a[:])
    return traspuesta(matriz)


def multmatrices(a, b):
    if len(a[0]) == len(b):
        matriz = [[[0, 0] for i in range(len(b[0]))] for j in range(len(a))]
        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(b)):
                    matriz[i][j] = suma(matriz[i][j], multiplicacion(a[i][k], b[k][j]))
        return matriz
    else:
        print("Debido a que las matrices no tienen tamaños compatibles, no es posible realizar la operación")


def productointerno(a, b):
    t = adjuntamatriz(a)
    vector = multmatrices(t, b)
    return vector


def normavector(a):
    rt = 0
    for i in range(len(a)):
        for j in range(len(a[0])):
            rt += a[i][j][0] ** 2 + a[i][j][1] ** 2
    return math.sqrt(rt)


#
#
def distanciavectores(a, b):
    v = restavectores(a, b)
    print(v)
    vector = normavector(v)
    print(vector)
    return vector


#
#
def matrizunitaria(a):
    t = adjuntamatriz(a)
    u = multmatrices(t, a)
    Identidad = np.identity(4)
    if Identidad == u:
        print("La matriz es unitaria")
        return u
    else:
        print("La matriz no es unitaria")
        return u


def matrizhermitiana(a):
    adj = adjuntamatriz(a)
    if adj == a:
        print("La matriz es hermitiana")
        return adj
    else:
        print("La matriz no es hermitiana")
        return adj



# Función printnumcomplejos: Escribe de una mejor manera el resultado de las operaciones de números complejos
# def printnumcomplejos(c):
# return print(str(round(c[0], 4)) + ' + ' + str(round(c[1], 4)) + 'i')


# Prueba de las diferentes funciones
# print(suma((1, 2), (2, 3)))
# print(inverso((2, 3)))
# resta((1, 2), (2, 3))
# multiplicacion((1, 2), (2, 3))
# division((2, 3), (3, 5))
# modulo(5, 2)
# conjugado(5, 2)
# polar(4, 3)
# cartesiano(8.246211251235321, 1.3258176636680326)
# fase(2, 5)
V1 = [[1, 2], [2, 3], [3, 4], [4, 5]]
V2 = [[2, 4], [4, 6], [8, 10], [12, 14]]
V3 = [[[1, 2]], [[2, 3]], [[3, 4]]]
V4 = [[[2, 3]], [[4, 1]], [[3, -4]]]
c = (2, -1)
# print(sumavectores(V1, V2))
# print(restavectores(V1, V2))
# print(inversovector(V1))
# print(multescalarvector(c, V2))
x = [
    [[1, 2], [2, 3], [1, 3]],
    [[4, 5], [5, 6], [6, 7]],
    [[2, 1], [5, 5], [4, 2]]
]
y = [
    [[2, 1], [3, 3], [1, 5]],
    [[2, 2], [3, 3], [5, 2]],
    [[1, 5], [2, 6], [7, 2]]
]
z = [
    [(5, 0), (3, 3), (1, 5)],
    [(3, -3), (3, 0), (2, 6)],
    [(1, -5), (2, -6), (3, 0)]
]

# print(sumamatrices(x, y))
# print(inversomatriz(x))
# print(multescalarmatriz(c, y))
# print(traspuesta(x))
# print(conjugadomatriz(y))
# print(adjuntamatriz(x))
# print(multmatrices(x, y))
# print(multmatrices(x, V3))
# print(productointerno(V3, V4))
# print(normavector(x))
# print(distanciavectores(V1, V2))
print(matrizunitaria(z))
print(matrizhermitiana(z))
