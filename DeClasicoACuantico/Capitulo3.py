import Libnumcomplex as lb
import math


# Experimento de las canicas con coeficientes booleanos, se tomará el 1 como True y el 0 como False.
# m: matriz doblemente estocastica unicamente con valores 1 y 0, v: vector con posiciones iniciales
# c: número de "clicks" que realiza, debe ser un número real
def expcanicas(m, v, c):
    for mult in range(c):
        v = lb.multmatrices(m, v)
    return v


# Experimento de las múltiples rendijas clásico probabilístico, con más de dos rendijas
# m: matriz doblemente estocastica con fraccionarios, v: vector con posiciones iniciales
# c: número de "clicks" que realiza, debe ser un número real
def expprobabilistico(m, v, c):
    for mult in range(c):
        v = lb.multmatrices(m, v)
    return v


# Experimento de las múltiples rendijas cuántico.
# m: matriz unitaria con números complejos, v: vector con posiciones iniciales
# c: número de "clicks" que realiza, debe ser un número real
def expcuantico(m, v, c):
    for mult in range(c):
        v = lb.multmatrices(m, v)
    return v


m1 = [
    [[0, 0], [1 / 6, 0], [5 / 6, 0]],
    [[1 / 3, 0], [1 / 2, 0], [1 / 6, 0]],
    [[2 / 3, 0], [1 / 3, 0], [0, 0]]
]
m2 = [
    [[0, 0], [1, 0], [0, 0]],
    [[1, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [1, 0]]
]
m3 = [
    [[1 / math.sqrt(2), 0], [1 / math.sqrt(2), 0], [0, 0]],
    [[0, -1 / math.sqrt(2)], [0, 1 / math.sqrt(2)], [0, 0]],
    [[0, 0], [0, 0], [0, 1]]
]
v1 = [
    [[1 / 6, 0]],
    [[1 / 6, 0]],
    [[2 / 3, 0]]
]
v2 = [
    [[2, 0]],
    [[4, 0]],
    [[4, 0]]
]
v3 = [
    [[1 / math.sqrt(3), 0]],
    [[0, 2 / math.sqrt(15)]],
    [[math.sqrt(2 / 5), 0]]
]
# print(expcanicas(m2, v2, 3))
# print(expprobabilistico(m1, v1, 1))
print(expcuantico(m3, v3, 1))
