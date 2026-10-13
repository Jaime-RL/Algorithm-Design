# -*- coding: utf-8 -*-

# 04_cod_07.py
#
# Clase para las soluciones parciales del problema «set
# cover», incluyendo una estrategia voraz.

import importlib

base = importlib.import_module("04_cod_03")


class Parcial_vrz(base.Parcial):
    def amplía_voraz(self):

        miembros = self.miembros
        habilidades = self.habilidades

        num_max = 0
        miembros_max = None

        for candidato in self.fichas:
            habilidades_candidato = candidato[1]
            habilidades_que_necesito = len(habilidades_candidato.difference(habilidades))

            if habilidades_que_necesito > num_max:
                num_max = habilidades_que_necesito
                miembros_max = candidato

        if miembros_max is not None:
            habilidades.update(miembros_max[1])
            miembros.append(int(miembros_max[0]))
             


