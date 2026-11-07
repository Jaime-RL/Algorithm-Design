"""La facultad de Königsberg de arriba abajo.

Enunciado: representar mediante un grafo no dirigido y no necesariamente
simple las plantas y los tramos de escalera de la facultad.
"""

import networkx as nx


def facultad():
    """Grafo de la facultad: los vértices son las plantas y las aristas
    los tramos de escalera. Es un MultiGraph porque puede haber varias
    escaleras entre las mismas dos plantas."""
    G = nx.MultiGraph()
    G.add_nodes_from(["0", "1", "2O", "2E", "3O", "3E"])

    # Planta baja - primera: 7 tramos
    for _ in range(7):
        G.add_edge("0", "1")

    # Parte oeste: 2 escaleras que suben hasta la tercera
    for _ in range(2):
        G.add_edge("1", "2O")
        G.add_edge("2O", "3O")

    # Parte este: 2 escaleras que suben hasta la tercera
    for _ in range(2):
        G.add_edge("1", "2E")
        G.add_edge("2E", "3E")

    return G


def plantas_impares(G):
    """Devuelve las plantas a las que llega un número impar de tramos."""
    return [v for v, d in G.degree() if d % 2 == 1]


# 1) ¿Es posible realizar un recorrido que recorra todos los tramos de
#    escalera una sola vez?

#    Grados: 0 -> 7, 1 -> 11, 2O -> 4, 2E -> 4, 3O -> 2, 3E -> 2.
#    Solo hay dos plantas con grado impar: la 0 y la 1.
#    SÍ se puede: empezando en la planta 0 y terminando en la 1 (o al revés).

# 2) ¿Es posible recorrer todos los tramos sin repetir ninguno, comenzando y
#    terminando además en el mismo lugar?

#    NO se puede volver al punto de partida, porque para eso todas las
#    plantas tendrían que tener grado par.

# 3) Responde también estas dos preguntas sobre el grafo resultante de
#    eliminar la planta baja.

#    Sin la planta baja desaparecen los 7 tramos 0-1 y los grados quedan:
#    1 -> 4, 2O -> 4, 2E -> 4, 3O -> 2, 3E -> 2. Todos pares.
#    Por tanto SÍ se puede recorrer todo, y además volviendo al mismo sitio.
#    Por ejemplo: 1 -> 2E -> 3E -> 2E -> 1 -> 2O -> 3O -> 2O -> 1

# Un camino euleriano recorre, sin repeticiones, todas las aristas de un grafo.
# Si además es circular, se denomina ciclo (o circuito) euleriano.

# 4) Deduce (o traduce) una caracterización de los grafos que contienen un
#    camino euleriano y otra de los grafos eulerianos.
#
#    Si el grafo es conexo:
#    - Tiene camino euleriano si tiene 0 o 2 vértices de grado impar.
#    - Es euleriano (el camino vuelve al inicio) si no tiene ninguno impar.

# 5) Escribe una función que devuelva True o False según el grafo de entrada
#    (que podría ser disconexo) sea o no euleriano. Puedes utilizar
#    is_connected, de NetworkX, pero no is_eulerian.
#
#    -> Está en ejercicio5.py (función euleriano_5).

# 6) Con las mismas condiciones, escribe una función que devuelva:
#    - False, si el grafo de entrada no tiene ningún camino euleriano;
#    - True, si es euleriano;
#    - una lista de los dos vértices que son los extremos de cualquier camino
#      euleriano en el grafo, en otro caso.

# 7) Describe un algoritmo que, tomando como entrada un grafo, construya un
#    camino euleriano, si lo hay.

# 8) Analiza la complejidad computacional de tu algoritmo.


if __name__ == "__main__":
    G = facultad()
    print("Número de tramos:", G.number_of_edges())
    print("Grados:", dict(G.degree()))
    print("Plantas con grado impar:", plantas_impares(G))

    # Pregunta 3: quitamos la planta baja
    H = facultad()
    H.remove_node("0")
    print("\nSin planta baja")
    print("Grados:", dict(H.degree()))
    print("Plantas con grado impar:", plantas_impares(H))

    from ejercicio5 import euleriano_5
    print("\n¿Facultad euleriana?", euleriano_5(G))
    print("¿Sin planta baja euleriana?", euleriano_5(H))
