"""Ejercicio 6: ¿tiene el grafo un camino euleriano?

Devuelve:
- False, si no hay ningún camino euleriano;
- True, si el grafo es euleriano (hay ciclo);
- [u, v], los dos extremos de cualquier camino euleriano, en otro caso.
"""
from ejercicio5 import aristas_conexas


def euleriano_6(G):
    if G.number_of_nodes() == 0:     # grafo vacío
        return False
    if not aristas_conexas(G):
        return False

    impares = [v for v, d in G.degree() if d % 2 == 1]
    if len(impares) == 0:            # todos pares: hay ciclo
        return True
    if len(impares) == 2:            # dos impares: camino de uno a otro
        return impares
    return False                     # más de dos impares: imposible
