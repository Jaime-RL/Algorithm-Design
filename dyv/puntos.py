"""
Utilidades comunes a todos los ejercicios de la práctica 07.

Un punto es una tupla (x, y). Todas las funciones que buscan la pareja
más próxima devuelven una tupla (distancia, p, q).
"""

import math
import sys

INFINITO = math.inf


def leer_puntos(nombre_fichero):
    """
    Lee un fichero con el formato que genera cod_07_05.py:

        <n> <dimensión>
        x1 y1
        x2 y2
        ...

    Devuelve una lista de tuplas (x, y).
    """
    with open(nombre_fichero) as f:
        n, dim = map(int, f.readline().split())
        if dim != 2:
            sys.exit('Solo se admiten puntos del plano (dimensión 2).')

        puntos = []
        for linea in f:
            if linea.strip():                      # saltamos líneas vacías
                x, y = map(float, linea.split())
                puntos.append((x, y))

    if len(puntos) != n:
        sys.exit(f'La cabecera dice {n} puntos, pero hay {len(puntos)}.')
    return puntos


def distancia(p, q):
    """Distancia euclídea entre dos puntos (solo usa x e y)."""
    return math.hypot(p[0] - q[0], p[1] - q[1])


def mejor(a, b):
    """De dos soluciones (d, p, q), devuelve la de menor distancia."""
    return a if a[0] <= b[0] else b


def mostrar(solucion):
    """Imprime la solución con el mismo aspecto que el enunciado."""
    d, p, q = solucion
    print(f'd(({p[0]:g}, {p[1]:g}), ({q[0]:g}, {q[1]:g})) = {d:g}')


def leer_argumentos(nombre_script):
    """Comprueba que el script se llama con un fichero de puntos."""
    if len(sys.argv) != 2:
        sys.exit(f'Uso: {nombre_script} <fichero de puntos>')
    puntos = leer_puntos(sys.argv[1])
    if len(puntos) < 2:
        sys.exit('Hacen falta al menos dos puntos.')
    return puntos
