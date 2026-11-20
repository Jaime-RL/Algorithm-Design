#! /usr/bin/env python3
"""
Comprueba que todos los algoritmos dan la MISMA distancia mínima que la
fuerza bruta (que hace de «oráculo») y mide tiempos.

Casos de prueba incluidos:
  * nubes aleatorias
  * rejillas (muchos puntos con la misma x y a la misma distancia: caso
    límite para la cota de 5 candidatos)
  * puntos repetidos y todos en una misma vertical
  * los ficheros de la práctica
"""

import random
import sys
import time

from puntos import leer_puntos
from cod_07_06 import fuerza_bruta
from ej05_particion import particion_mediana, particion_ordenando
from ej09_bandas import pareja_mas_proxima_bandas
from ej10_shamos_strong import pareja_mas_proxima
from ej11_cormen import pareja_mas_proxima_cormen

sys.setrecursionlimit(10_000)

ALGORITMOS = {
    'bandas (ej 9)': pareja_mas_proxima_bandas,
    'Shamos (ej 10)': pareja_mas_proxima,
    'Cormen (ej 11)': pareja_mas_proxima_cormen,
}


def comprobar(puntos, nombre_caso):
    esperado = fuerza_bruta(puntos)[0]
    for nombre, algoritmo in ALGORITMOS.items():
        obtenido = algoritmo(puntos)[0]
        assert abs(obtenido - esperado) < 1e-9, \
            f'{nombre} falla en {nombre_caso}: {obtenido} != {esperado}'


def comprobar_particiones(puntos):
    for funcion in (particion_ordenando, particion_mediana):
        P1, P2, x0 = funcion(puntos)
        assert abs(len(P1) - len(P2)) <= 1
        assert sorted(P1 + P2) == sorted(puntos)
        assert all(p[0] <= x0 for p in P1) and all(p[0] >= x0 for p in P2)


def pruebas_aleatorias():
    random.seed(7)
    for _ in range(300):
        n = random.randint(2, 120)
        nube = [(random.randint(0, 30), random.randint(0, 30)) for _ in range(n)]
        comprobar(nube, 'aleatorio entero')
        comprobar_particiones(nube)

        nube = [(random.random(), random.random()) for _ in range(n)]
        comprobar(nube, 'aleatorio real')

    for lado in range(2, 16):                  # rejillas lado x lado
        rejilla = [(i, j) for i in range(lado) for j in range(lado)]
        random.shuffle(rejilla)
        comprobar(rejilla, f'rejilla {lado}x{lado}')

    for n in range(2, 60):                     # todos en la misma vertical
        comprobar([(0, 3 * k) for k in range(n)], 'vertical')
    comprobar([(1, 1)] * 10 + [(5, 5)], 'repetidos')
    print('Todas las pruebas de corrección superadas.')


def ficheros():
    print('\nFicheros de la práctica')
    for fichero in ('ej_pts_01.txt', 'ej_pts_02.txt', 'ej_pts_03.txt'):
        puntos = leer_puntos('datos/' + fichero)
        print(f'\n  {fichero}  (n = {len(puntos)})')
        for nombre, algoritmo in [('fuerza bruta', fuerza_bruta), *ALGORITMOS.items()]:
            inicio = time.perf_counter()
            d, p, q = algoritmo(puntos)
            t = time.perf_counter() - inicio
            print(f'    {nombre:<15} d = {d:<10g} {p} - {q}   {t:7.3f} s')


def tiempos():
    print('\nTiempos con nubes aleatorias (segundos)')
    print(f'  {"n":>7} {"fuerza bruta":>13} {"Shamos":>9} {"Cormen":>9}')
    random.seed(1)
    for n in (500, 1000, 2000, 4000, 8000, 16000, 100000):
        nube = [(random.random(), random.random()) for _ in range(n)]
        fila = []
        for algoritmo in (fuerza_bruta, pareja_mas_proxima, pareja_mas_proxima_cormen):
            if algoritmo is fuerza_bruta and n > 4000:
                fila.append('   -   ')
                continue
            inicio = time.perf_counter()
            algoritmo(nube)
            fila.append(f'{time.perf_counter() - inicio:7.3f}')
        print(f'  {n:>7} {fila[0]:>13} {fila[1]:>9} {fila[2]:>9}')


if __name__ == '__main__':
    pruebas_aleatorias()
    ficheros()
    tiempos()
