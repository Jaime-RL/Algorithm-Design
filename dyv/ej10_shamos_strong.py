#! /usr/bin/env python3
"""
Ejercicio 10 — Algoritmo de SHAMOS y STRONG en O(n log n).

PREPROCESO (una sola vez, O(n log n)):
    X = puntos ordenados por x
    Y = los mismos puntos ordenados por y

PASO RECURSIVO sobre (X, Y), todo en O(n) salvo las llamadas recursivas:
    a) Separar X en X1 y X2 (ejercicio 7)                         O(n)
    b) Separar Y en Y1 e Y2 FILTRANDO: se conserva el orden por y  O(n)
    c) Recursión en (X1, Y1) y (X2, Y2)  ->  delta = mín(d1, d2)
    d) Bandas B1 (de Y1) y B2 (de Y2) por su ABSCISA:              O(n)
           B1: x > x0 - delta      B2: x < x0 + delta
       (el enunciado dice «ordenada» en este paso: es una errata)
    e) Recorrer las bandas una sola vez, con dos índices,
       mirando solo 5 candidatos de B2 por cada punto de B1        O(n)

Recurrencia: T(n) = 2 T(n/2) + Θ(n)  ->  T(n) = Θ(n log n)

DETALLE IMPORTANTE (paso b): si decidimos el lado de un punto de Y solo
mirando «x < x0», los puntos con x == x0 se reparten mal (pueden estar
en X1 o en X2). Por eso cada punto lleva una ETIQUETA (su índice en la
entrada) y Y1 se forma con los puntos cuya etiqueta está en X1. Además,
así funcionan también los puntos repetidos.

Internamente cada punto es (x, y, etiqueta).
"""

import sys
import time

from puntos import distancia, leer_argumentos, mejor, mostrar
from cod_07_06 import fuerza_bruta
from ej07_particion_ordenada import particion_ordenada

CASO_BASE = 3
CANDIDATOS = 5     # como mucho 5 puntos de P2 en el rectángulo [x0, x0+δ) × (py-δ, py+δ)


def combinar(B1, B2, sol):
    """
    Paso (e). B1 y B2 están ordenadas por y.

    Para cada p = B1[i]:
      - avanzamos j (nunca retrocede) mientras B2[j] esté demasiado abajo
        (y <= py - delta): ese q tampoco servirá para los siguientes p,
        porque los p van subiendo;
      - comparamos p con los CANDIDATOS siguientes de B2.

    i recorre B1 una vez y j recorre B2 una vez  ->  O(|B1| + |B2|).
    """
    i, j = 0, 0
    while i < len(B1):
        p = B1[i]
        delta = sol[0]

        # Comprobamos j < len(B2) ANTES de acceder a B2[j]
        # (en el pseudocódigo del enunciado ese orden está al revés)
        while j < len(B2) and B2[j][1] <= p[1] - delta:
            j += 1
        if j >= len(B2):
            break

        for k in range(j, min(j + CANDIDATOS, len(B2))):
            d = distancia(p, B2[k])
            if d < sol[0]:
                sol = (d, p, B2[k])
        i += 1
    return sol


def recursivo(X, Y):
    """X ordenada por x, Y ordenada por y, con los mismos puntos."""

    # Caso base
    if len(X) <= CASO_BASE:
        return fuerza_bruta(X)

    # a) Dividir X
    X1, X2, x0 = particion_ordenada(X)

    # b) Dividir Y conservando su orden
    en_X1 = {p[2] for p in X1}                 # etiquetas de la mitad izquierda
    Y1 = [p for p in Y if p[2] in en_X1]
    Y2 = [p for p in Y if p[2] not in en_X1]

    # c) Resolver cada mitad
    sol = mejor(recursivo(X1, Y1), recursivo(X2, Y2))
    delta = sol[0]
    if delta == 0:                             # puntos repetidos: imposible mejorar
        return sol

    # d) Bandas (ordenadas por y porque salen de Y1 e Y2)
    B1 = [p for p in Y1 if p[0] > x0 - delta]
    B2 = [q for q in Y2 if q[0] < x0 + delta]

    # e) Parejas mixtas en tiempo lineal
    return combinar(B1, B2, sol)


def pareja_mas_proxima(puntos):
    """Preproceso + llamada recursiva. Devuelve (d, p, q) con p, q = (x, y)."""
    etiquetados = [(x, y, i) for i, (x, y) in enumerate(puntos)]
    X = sorted(etiquetados, key=lambda p: p[0])
    Y = sorted(etiquetados, key=lambda p: p[1])

    d, p, q = recursivo(X, Y)
    return d, p[:2], q[:2]                     # quitamos la etiqueta


if __name__ == '__main__':
    puntos = leer_argumentos('ej10_shamos_strong.py')

    inicio = time.perf_counter()
    solucion = pareja_mas_proxima(puntos)
    fin = time.perf_counter()

    mostrar(solucion)
    print(f'(n = {len(puntos)}, tiempo = {fin - inicio:.3f} s)')
