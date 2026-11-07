"""Ejercicio 5: ¿es euleriano el grafo? (puede ser disconexo)"""
import networkx as nx


def aristas_conexas(G):
    """True si todas las aristas están en una misma componente conexa.
    Los vértices aislados (sin aristas) no impiden el recorrido, así que
    los quitamos antes de comprobar si es conexo."""
    con_aristas = [v for v in G if G.degree(v) > 0]
    if len(con_aristas) == 0:
        return True
    return nx.is_connected(G.subgraph(con_aristas))


def euleriano_5(G):
    if G.number_of_nodes() == 0:     # grafo vacío: lo consideramos no euleriano
        return False
    if not aristas_conexas(G):
        return False
    for v, d in G.degree():
        if d % 2 == 1:
            return False
    return True
