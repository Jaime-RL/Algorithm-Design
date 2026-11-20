#! /usr/bin/env python3
"""
Ejercicio 9 — Divide y vencerás con FUERZA BRUTA EN LAS BANDAS.

  Preproceso:  ordenar los puntos por x (una sola vez)       O(n log n)
  Dividir:     cortar por la mitad (ejercicio 7)
  Resolver:    recursión en cada mitad  ->  delta = mín(d1, d2)
  Combinar:    probar TODAS las parejas mixtas (p en B1, q en B2), con
                  B1 = puntos de X1 con  x0 - delta < x <= x0
                  B2 = puntos de X2 con  x0 <= x < x0 + delta

Es correcto (ejercicio 8), pero NO mejora el caso peor: si todos los
puntos caen en las bandas, combinar cuesta |B1|·|B2| = Θ(n²) y por el
teorema maestro T(n) = Θ(n²).

El fichero ej_pts_01.txt está construido justo así: casi todos los
puntos tienen x ≈ 10 (la divisoria), muy separados en vertical.
"""

import sys
import time

from puntos import distancia, leer_argumentos, mejor, mostrar
from cod_07_06 import fuerza_bruta
from ej07_particion_ordenada import particion_ordenada

CASO_BASE = 3          # con 3 puntos o menos, fuerza bruta directamente

contador_parejas_mixtas = 0     # solo para ver cuánto trabajo hace la combinación


def recursivo(X):
    """X tiene al menos 2 puntos y está ordenada por x."""
    global contador_parejas_mixtas

    # 1) Caso base
    if len(X) <= CASO_BASE:
        return fuerza_bruta(X)

    # 2) Dividir
    X1, X2, x0 = particion_ordenada(X)

    # 3) Resolver cada mitad
    sol = mejor(recursivo(X1), recursivo(X2))
    delta = sol[0]

    # 4) Combinar: bandas de anchura delta a cada lado de x = x0
    B1 = [p for p in X1 if p[0] > x0 - delta]
    B2 = [q for q in X2 if q[0] < x0 + delta]

    for p in B1:                       # fuerza bruta entre las dos bandas
        for q in B2:
            contador_parejas_mixtas += 1
            d = distancia(p, q)
            if d < sol[0]:
                sol = (d, p, q)
    return sol


def pareja_mas_proxima_bandas(puntos):
    X = sorted(puntos, key=lambda p: p[0])      # preproceso
    return recursivo(X)


if __name__ == '__main__':
    sys.setrecursionlimit(10_000)
    puntos = leer_argumentos('ej09_bandas.py')

    inicio = time.perf_counter()
    solucion = pareja_mas_proxima_bandas(puntos)
    fin = time.perf_counter()

    mostrar(solucion)
    print(f'parejas mixtas comprobadas: {contador_parejas_mixtas}  '
          f'(n = {len(puntos)}, tiempo = {fin - inicio:.2f} s)')
