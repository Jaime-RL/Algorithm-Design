# -*- coding: utf-8 -*-

# Este módulo proporciona generadores para los grafos (no
# dirigidos) y para los grafos dirigidos en n vértices no
# etiquetados.
#
# Estos generadores almacenan en memoria los grafos ya
# calculados y, basándose en los generadores etiquetados
# correspondientes, comprueban para cada nuevo elemento si
# ya se ha generado un grafo isomorfo, descartándolo en ese
# caso.

#import importlib

import networkx as nx


import ej1 as m1
import ej2 as m2

#m1 = importlib.import_module("ej1")
#m2 = importlib.import_module("ej2")


def ya_esta(g, lista):
    """Decide si en lista ya hay un grafo isomorfo a g."""

    # -*- coding: utf-8 -*-

    # Este módulo proporciona generadores para los grafos (no
    for h in lista:
        if nx.is_isomorphic(g, h):
            return True
    return False


def no_etiq(generador):
    lista = list()
    for g in generador:
        if not ya_esta(g, lista):
            yield g
            lista.append(g)


def iterator_no_d_no_etiq(n):
    yield from m1.no_d_etiq(n)

def no_d_no_etiq(n):
    iterator = iterator_no_d_no_etiq(n)
    lista = list()

    while (a:=next(iterator)) not in lista:
        yield a
        lista.append(a)


def d_no_etiq(n):
    lista = list()
    # retornar todos los grafos  NO  etiquetados


    for g in m2.d_etiq(n):
        if not ya_esta(g, lista):
            lista.append(g)

    return lista


