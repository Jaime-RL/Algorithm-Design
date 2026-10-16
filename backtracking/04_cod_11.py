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

        habilidades_restantes = set(range(self.cardinal))

        # poda -> cota inferior
        habilidades_restantes = habilidades_restantes.difference(self.habilidades)
        maximo = max(len(habs-self.habilidades) for _,habs in self.fichas)
        # error en la division
        numero_personas_min = math.ceil(habilidades_restantes / maximo)

        cota_inferior = self.coste() + numero_personas_min

        return cota_inferior

    






