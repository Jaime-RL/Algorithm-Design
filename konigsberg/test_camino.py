import networkx as nx
from ejercicio7 import construir_camino

def test_sencillo():
    G = nx.MultiGraph()
    G.add_edge("A", "B")
    G.add_edge("B", "C")
    G.add_edge("C", "D")
    assert construir_camino(G) == ["A","B", "C", "D"]

def test_una_arista():
    G = nx.MultiGraph()
    G.add_edge("A", "B")
    assert construir_camino(G) == ["A","B"]
    
def test_grafo_un_vertice_sin_aristas():
    G = nx.MultiGraph()
    G.add_node("A")
    assert construir_camino(G) == ["A"]

def test_grafo_vacio():
    assert construir_camino(nx.MultiGraph()) == False
    
def test_grafo_sin_camino():
    G = nx.MultiGraph()
    G.add_edge("A", "B")
    G.add_edge("B", "C")
    G.add_edge("B", "H")
    assert construir_camino(G) == False
    
def test_grafo_ejercicio():
    G = nx.MultiGraph()
    G.add_edge("A", "B")
    G.add_edge("A", "B")
    G.add_edge("A", "B")
    G.add_edge("A", "B")
    G.add_edge("B", "C")
    G.add_edge("B", "C")
    G.add_edge("B", "D")
    G.add_edge("B", "D")
    G.add_edge("C", "E")
    G.add_edge("C", "E")
    G.add_edge("D", "F")
    G.add_edge("D", "F")
    assert construir_camino(G) == ['A', 'B', 'A', 'B', 'C', 'E', 'C', 'B', 'D', 'F', 'D', 'B', 'A']