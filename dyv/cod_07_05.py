#! /usr/bin/env python3

# Este programa genera puntos *no repetidos* en un
# rectángulo del plano.

refinamiento = 100000

import sys
import os
import random

def tirada(cota):
    x = random.randrange(0, refinamiento) * cota
    return  x / refinamiento

def escribe_puntos(S, fich):
    if os.access(fich, os.F_OK):
        print('El fichero ‘' + fich + '’ ya existe.')
    else:
        f = open(fich, 'w')
        L = list(S)
        d = len(L[0])
        f.write('{} {}\n'.format(len(S), d))
        for p in L:
            for x in p[:-1]:
                f.write('{0:g} '.format(x))
                f.write('{0:g}\n'.format(p[-1]))
        f.close()

def genera_puntos(n, d, cotas_inf, cotas_sup):
    S = set()
    while len(S) < n:
        p = list()
        for i in range(d):
            x = cotas_inf[i] + \
                tirada(cotas_sup[i] - cotas_inf[i])
            p.append(x)
        S.add(tuple(p))
    return S

if __name__ == '__main__':
    try:
        n = int(sys.argv[1])
        cotas_inf = list()
        cotas_sup = list()
        j = 2
        for i in range(2):
            cotas_inf.append(float(sys.argv[j]))
            j += 1
            cotas_sup.append(float(sys.argv[j]))
            j += 1
        fich = sys.argv[j]
    except:
        sys.exit('cod_07_05 <n.º puntos> <x_min> <x_max> <y_min> '
                 '<y_max> <fichero de salida>')
    S = genera_puntos(n, 2, cotas_inf, cotas_sup)
    escribe_puntos(S, fich)
