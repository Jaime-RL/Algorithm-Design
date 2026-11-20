#! /usr/bin/env python3
"""
Ejercicio 5 — Partir una lista de puntos en dos mitades P1 y P2 tales que

    | |P1| - |P2| | <= 1
    existe x0 con:  todo (x, y) de P1 cumple x <= x0
                    todo (x, y) de P2 cumple x >= x0

Se proponen dos vías:

  A) ORDENAR por abscisa y cortar por la mitad          ->  O(n log n)
  B) Calcular la MEDIANA de las abscisas y repartir     ->  O(n) esperado

¡Ojo con la vía B! statistics.median() ordena la lista internamente,
así que en CPython cuesta O(n log n), no O(n). Para conseguir de verdad
tiempo lineal hay que usar un algoritmo de selección. Aquí usamos
QUICKSELECT (O(n) en tiempo esperado). Con «mediana de medianas»
(Blum et al.) se obtiene O(n) también en el caso peor.
"""

import statistics


# ---------------------------------------------------------------------
# Vía A: ordenación
# ---------------------------------------------------------------------
def particion_ordenando(puntos):
    """O(n log n): ordenamos por x y cortamos por el centro."""
    ordenados = sorted(puntos, key=lambda p: p[0])
    mitad = len(ordenados) // 2
    P1, P2 = ordenados[:mitad], ordenados[mitad:]
    x0 = P2[0][0]               # vale cualquier x entre el último de P1 y el primero de P2
    return P1, P2, x0


# ---------------------------------------------------------------------
# Vía B: mediana
# ---------------------------------------------------------------------
def particion_mediana(puntos):
    """
    O(n log n): statistics.median ordena internamente; el reparto es O(n).

    El caso delicado son los puntos con x == x0 (puede haber muchos con
    la misma abscisa). No se pueden mandar todos al mismo lado, porque
    las mitades quedarían desequilibradas. Los repartimos: primero
    rellenamos P1 hasta que tenga n//2 elementos y el resto va a P2.
    """
    n = len(puntos)
    x0 = statistics.median(p[0] for p in puntos)

    izquierda   = [p for p in puntos if p[0] < x0]
    derecha     = [p for p in puntos if p[0] > x0]
    en_la_recta = [p for p in puntos if p[0] == x0]

    faltan = n // 2 - len(izquierda)
    P1 = izquierda + en_la_recta[:faltan]
    P2 = en_la_recta[faltan:] + derecha
    return P1, P2, x0


# ---------------------------------------------------------------------
# Pequeña demostración
# ---------------------------------------------------------------------
if __name__ == '__main__':
    # Caso con abscisas repetidas: el que rompe las desigualdades estrictas (ej. 4)
    nube = [(1, 0), (2, 5), (2, 1), (2, 3), (2, 7), (3, 2), (4, 4)]

    for nombre, funcion in [('ordenando', particion_ordenando),
                            ('mediana  ', particion_mediana)]:
        P1, P2, x0 = funcion(nube)
        print(f'{nombre}: x0 = {x0}  |P1| = {len(P1)}  |P2| = {len(P2)}')
        print(f'           P1 = {sorted(P1)}')
        print(f'           P2 = {sorted(P2)}')
