#! /usr/bin/env python3
"""
Ejercicio 7 — Partición suponiendo que la lista YA está ordenada por x.

Si la entrada está ordenada por abscisa no decreciente, basta cortarla
por el índice central:

  * los tamaños difieren como mucho en 1                 (n//2 y n - n//2)
  * las dos mitades siguen ordenadas                      (son trozos contiguos)
  * x0 = abscisa del primer punto de P2 sirve de divisoria:
        todo P1 tiene x <= x0   y   todo P2 tiene x >= x0

Coste: O(n) por la copia de los trozos (con índices sería O(1)).
"""


def particion_ordenada(X):
    """X está ordenada por x. Devuelve (X1, X2, x0)."""
    mitad = len(X) // 2
    X1, X2 = X[:mitad], X[mitad:]
    x0 = X2[0][0]
    return X1, X2, x0


if __name__ == '__main__':
    X = [(0, 1), (1, 4), (1, 2), (3, 0), (5, 5), (6, 1), (9, 3)]
    X1, X2, x0 = particion_ordenada(X)
    print('X1 =', X1)
    print('X2 =', X2)
    print('x0 =', x0)
