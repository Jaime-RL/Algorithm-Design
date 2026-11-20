#! /usr/bin/env python3
"""
Ejercicio 2 — Pareja más próxima por FUERZA BRUTA.

Idea: probar todas las parejas (i, j) con i < j y quedarse con la mejor.

Coste (ejercicio 3): hay n(n-1)/2 parejas y cada una cuesta O(1)
  ->  Θ(n²)

Uso:
    ./cod_07_05.py 1000 0 10 0 10 puntos.txt
    ./cod_07_06.py puntos.txt
"""

from puntos import INFINITO, distancia, leer_argumentos, mostrar


def fuerza_bruta(puntos):
    """Devuelve (d, p, q) con la pareja más próxima de la lista."""
    mejor_d, mejor_p, mejor_q = INFINITO, None, None
    n = len(puntos)

    for i in range(n):
        for j in range(i + 1, n):          # j > i: cada pareja una sola vez
            d = distancia(puntos[i], puntos[j])
            if d < mejor_d:
                mejor_d, mejor_p, mejor_q = d, puntos[i], puntos[j]

    return mejor_d, mejor_p, mejor_q


if __name__ == '__main__':
    mostrar(fuerza_bruta(leer_argumentos('cod_07_06.py')))
