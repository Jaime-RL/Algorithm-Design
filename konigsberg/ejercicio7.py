"""Ejercicio 7: construir un camino euleriano, si lo hay.

Algoritmo de Hierholzer. Devuelve la lista de vértices del camino (o del
ciclo, si el grafo es euleriano), o False si no hay camino euleriano.
"""
from ejercicio6 import euleriano_6


def vertice_inicial(G):
    """Dónde empezar: en uno de los dos vértices impares si los hay; si no,
    en cualquier vértice con aristas (o en el único que haya)."""
    tipo = euleriano_6(G)
    if tipo is False:
        return None
    if isinstance(tipo, list):       # hay dos impares: empezamos en uno
        return tipo[0]
    for v in G:                      # todos pares: cualquiera con aristas
        if G.degree(v) > 0:
            return v
    return next(iter(G))             # grafo sin aristas


def construir_camino(G):
    inicio = vertice_inicial(G)
    if inicio is None:
        return False

    # Para cada vértice, lista de (vecino, número de arista). Numeramos las
    # aristas para distinguir las repetidas del MultiGraph.
    vecinos = {v: [] for v in G}
    for i, (u, v) in enumerate(G.edges()):
        vecinos[u].append((v, i))
        vecinos[v].append((u, i))
    for v in vecinos:
        vecinos[v].reverse()         # para sacarlas con pop() en orden
    usada = [False] * G.number_of_edges()

    pila = [inicio]
    camino = []
    while pila:
        v = pila[-1]
        # quitamos de la lista las aristas que ya hemos usado
        while vecinos[v] and usada[vecinos[v][-1][1]]:
            vecinos[v].pop()
        if vecinos[v]:
            # queda alguna arista sin usar: la recorremos
            w, i = vecinos[v].pop()
            usada[i] = True
            pila.append(w)
        else:
            # nos hemos atascado: v pasa al camino
            camino.append(pila.pop())

    camino.reverse()
    return camino
