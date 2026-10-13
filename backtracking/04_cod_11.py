import importlib
import math

base = importlib.import_module("04_cod_03")
extra = importlib.import_module("04_cod_07")

# optimizacion con maximos locales. iniciamos el alg con un dict que cuente
# cuantas personas con cierto numero de habilidades tienen; ej: 10: 4 6: 8
# debemos de llevar cuenta de cuando hemos empleado el maximo y utilizamos 
# el siguiente maximo local para calcular la cota inferior. 

class Parcial_ct(base.Parcial):

    def cota(self):

        miembros = self.miembros
        habilidades = self.habilidades

        mejor_equipo_CS = extra.Parcial_vrz("04_dat_01.txt").voraz()

        habilidades_obtenidas = list()
        habilidades_restantes = [i for i in range(136)]

        candidatos_evaluados = 0
        tamaño_equipo = 0

        # casos base
        if len(habilidades_obtenidas) == 137:
            return self

        if candidatos_evaluados == len(self.fichas):
            return self

        # poda -> cota inferior
        habilidades_restantes = habilidades_restantes.difference(habilidades_obtenidas)
        numero_personas_min = math.ceil(habilidades_restantes / 10)

        cota_inferior = tamaño_equipo + numero_personas_min
        
        if cota_inferior >= mejor_equipo_CS:




