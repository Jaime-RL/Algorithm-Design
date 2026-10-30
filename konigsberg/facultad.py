"""La facultad de Königsberg de arriba abajo.

Enunciado: representar mediante un grafo no dirigido y no necesariamente
simple las plantas y los tramos de escalera de la facultad.
"""

# 1) ¿Es posible realizar un recorrido que recorra todos los tramos de
#    escalera una sola vez?

# 2) ¿Es posible recorrer todos los tramos sin repetir ninguno, comenzando y
#    terminando además en el mismo lugar?

# 3) Responde también estas dos preguntas sobre el grafo resultante de
#    eliminar la planta baja.

# Un camino euleriano recorre, sin repeticiones, todas las aristas de un grafo.
# Si además es circular, se denomina ciclo (o circuito) euleriano.

# 4) Deduce (o traduce) una caracterización de los grafos que contienen un
#    camino euleriano y otra de los grafos eulerianos.

# 5) Escribe una función que devuelva True o False según el grafo de entrada
#    (que podría ser disconexo) sea o no euleriano. Puedes utilizar
#    is_connected, de NetworkX, pero no is_eulerian.

# 6) Con las mismas condiciones, escribe una función que devuelva:
#    - False, si el grafo de entrada no tiene ningún camino euleriano;
#    - True, si es euleriano;
#    - una lista de los dos vértices que son los extremos de cualquier camino
#      euleriano en el grafo, en otro caso.

# 7) Describe un algoritmo que, tomando como entrada un grafo, construya un
#    camino euleriano, si lo hay.

# 8) Analiza la complejidad computacional de tu algoritmo.
