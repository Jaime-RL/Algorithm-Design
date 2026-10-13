# -*- coding: utf-8 -*-

# Este módulo genera todos los grafos dirigidos en n
# vértices etiquetados.
#
# Los obtiene, de modo iterativo, a través de las posibles
# matrices de adyacencia con entradas 0/1 y ceros en la
# diagonal.

import networkx as nx
import numpy as np


def matriz(dim, n):
    """Devuelve una matriz (numpy) cuadrada y extradiagonal,
    con entradas 0/1, ceros en la diagonal y el resto de las
    entradas tomadas de los bits de n.
    """

    M = np.zeros([dim, dim], dtype=int)

    for i in range(dim):
        for j in range(dim):
            if i == j:
                continue

            M[i,j] = n % 2
            n = n // 2

    return M


def dir(M):
    """Devuelve el gr. dirigido asociado a la matriz M."""

    return nx.from_numpy_matrix(M, create_using=nx.DiGraph())


def d_etiq(n):
    """Generador de los grafos dirigidos en n vértices
    etiquetados.
    """

    huecos = n * (n - 1)
    N = 2**huecos
    for i in range(N):
        yield dir(matriz(n, i))



