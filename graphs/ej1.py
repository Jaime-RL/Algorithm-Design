# -*- coding: utf-8 -*-

# Este módulo genera todos los grafos (no dirigidos) en n
# vértices etiquetados.
#
# Los obtiene, de modo iterativo, a través de las posibles
# matrices de adyacencia con entradas 0/1 en la parte
# triangular superior.

import networkx as nx
import numpy as np


def matriz(dim, n):
    """Devuelve una matriz (numpy) cuadrada y triangular
    superior, con entradas 0/1, ceros en la diagonal y el
    resto de las entradas tomadas de los bits de n.
    """

    M = np.zeros([dim, dim], dtype=int)

    for i in range(dim):
        for j in range(i+1, dim):
            M[i,j] = n % 2
            n = n // 2
            M[j,i] = M[i,j]
    
    return M


def no_dir(M):
    """Devuelve el gr. (no dirigido) asoc. a la matriz M."""

    return nx.from_numpy_matrix(M, create_using=nx.Graph())


def no_d_etiq(n):
    """Generador de los grafos (no dirigidos) en n vértices
    etiquetados.
    """

    huecos = int(n * (n - 1) / 2)
    N = 2**huecos
    for i in range(N):
        yield no_dir(matriz(n, i))



