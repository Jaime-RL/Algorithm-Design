#! /usr/bin/env python3
"""
Ejercicio 11 — Variante de CORMEN et al. (§ 33.4).

Diferencia con el ejercicio 10: en lugar de dos bandas separadas,
juntamos en UNA sola lista Y' todos los puntos de Y con |x - x0| < delta
(ordenados por y) y comparamos cada punto con los 5 siguientes de la
lista, SIN mirar en qué lado están.

¿Por qué no hay que mirar el lado? Si una pareja mejora delta, sus dos
puntos están necesariamente en lados distintos: dos puntos del mismo
lado están a distancia >= delta por definición de delta.

Mismo coste: T(n) = 2 T(n/2) + Θ(n) = Θ(n log n), código más corto.

(Cormen propone primero 7 comparaciones por punto; el ejercicio 33.4-2
del libro reduce la cantidad a 5.)
"""

import time

from puntos import distancia, leer_argumentos, mejor, mostrar
from cod_07_06 import fuerza_bruta
from ej07_particion_ordenada import particion_ordenada

CASO_BASE = 3
SIGUIENTES = 5


def recursivo(X, Y):
    if len(X) <= CASO_BASE:
        return fuerza_bruta(X)

    # Dividir X y, conservando el orden, también Y
    X1, X2, x0 = particion_ordenada(X)
    en_X1 = {p[2] for p in X1}
    Y1 = [p for p in Y if p[2] in en_X1]
    Y2 = [p for p in Y if p[2] not in en_X1]

    # Resolver
    sol = mejor(recursivo(X1, Y1), recursivo(X2, Y2))
    delta = sol[0]

    # Combinar: una única franja, ordenada por y
    franja = [p for p in Y if abs(p[0] - x0) < delta]

    for i in range(len(franja)):
        for k in range(i + 1, min(i + 1 + SIGUIENTES, len(franja))):
            d = distancia(franja[i], franja[k])
            if d < sol[0]:
                sol = (d, franja[i], franja[k])
    return sol


def pareja_mas_proxima_cormen(puntos):
    etiquetados = [(x, y, i) for i, (x, y) in enumerate(puntos)]
    X = sorted(etiquetados, key=lambda p: p[0])
    Y = sorted(etiquetados, key=lambda p: p[1])
    d, p, q = recursivo(X, Y)
    return d, p[:2], q[:2]


if __name__ == '__main__':
    puntos = leer_argumentos('ej11_cormen.py')

    inicio = time.perf_counter()
    solucion = pareja_mas_proxima_cormen(puntos)
    fin = time.perf_counter()

    mostrar(solucion)
    print(f'(n = {len(puntos)}, tiempo = {fin - inicio:.3f} s)')
