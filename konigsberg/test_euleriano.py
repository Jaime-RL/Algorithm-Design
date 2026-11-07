import networkx as nx
from ejercicio5 import euleriano_5
from ejercicio6 import euleriano_6

def test_grafo_ejercicio5():
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
    assert euleriano_5(G) == True

def test_grafo_ejercicio6():
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
    assert euleriano_6(G) == True
    
def test_grafo_impar_5():
    G = nx.MultiGraph()
    G.add_edge("A", "B")
    G.add_edge("B", "C")
    G.add_edge("B", "C")
    assert euleriano_5(G) == False

def test_grafo_impar_6():
    G = nx.MultiGraph()
    G.add_edge("A", "B")
    G.add_edge("B", "C")
    G.add_edge("B", "C")
    assert euleriano_6(G) == ["A", "B"]
    
def test_grafo_inconexo_5():
    G = nx.MultiGraph()
    G.add_edge("A", "B")
    G.add_edge("B", "C")
    G.add_edge("C", "A")
    G.add_edge("D", "E")
    G.add_edge("E", "F")
    G.add_edge("F", "D")
    assert euleriano_5(G) == False

def test_grafo_inconexo_6():
    G = nx.MultiGraph()
    G.add_edge("A", "B")
    G.add_edge("B", "C")
    G.add_edge("C", "A")
    G.add_edge("D", "E")
    G.add_edge("E", "F")
    G.add_edge("F", "D")
    assert euleriano_6(G) == False
    
def test_grafo_sin_camino_5():
    G = nx.MultiGraph()
    G.add_edge("A", "B")
    G.add_edge("B", "C")
    G.add_edge("B", "H")
    assert euleriano_5(G) == False
    
def test_grafo_sin_camino_6():
    G = nx.MultiGraph()
    G.add_edge("A", "B")
    G.add_edge("B", "C")
    G.add_edge("B", "H")
    assert euleriano_6(G) == False
    
def test_grafo_vacio_5():
    assert euleriano_5(nx.MultiGraph()) == False

def test_grafo_vacio_6():
    assert euleriano_6(nx.MultiGraph()) == False

def test_grafo_un_vertice_sin_aristas_5():
    G = nx.MultiGraph()
    G.add_node("A")
    assert euleriano_5(G) == True
    
def test_grafo_un_vertice_sin_aristas_6():
    G = nx.MultiGraph()
    G.add_node("A")
    assert euleriano_5(G) == True

def test_una_arista_5():
    G = nx.MultiGraph()
    G.add_edge("A", "B")
    assert euleriano_5(G) == False

def test_una_arista_6():
    G = nx.MultiGraph()
    G.add_edge("A", "B")
    assert euleriano_6(G) == ["A","B"]
