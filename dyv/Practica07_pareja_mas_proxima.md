---
tags: [DA, divide-y-venceras, geometria-computacional, practica]
asignatura: G682 Diseño de Algoritmos
---

# Práctica 07 (hoja B): la pareja más próxima

> [!summary] Idea en una línea
> Fuerza bruta: **Θ(n²)**. Divide y vencerás (Shamos y Strong) con preproceso (X ordenada por x, Y ordenada por y) y combinación lineal: **Θ(n log n)**, que es óptimo en el modelo de comparaciones.

## Ficheros

| Fichero | Ejercicio | Qué hace |
|---|---|---|
| `puntos.py` | — | Lectura del fichero, distancia, impresión |
| `cod_07_06.py` | 2, 3 | Fuerza bruta |
| `ej05_particion.py` | 5 | Partición por ordenación y por mediana (quickselect) |
| `ej07_particion_ordenada.py` | 7 | Partición de una lista ya ordenada por x |
| `ej09_bandas.py` | 9 | D&V con fuerza bruta en las bandas |
| `ej10_shamos_strong.py` | 10 | Algoritmo completo O(n log n) |
| `ej11_cormen.py` | 11 | Variante de Cormen (una sola franja) |
| `pruebas.py` | — | Compara todo con la fuerza bruta y mide tiempos |

```bash
./cod_07_05.py 1000 0 10 0 10 puntos.txt   # n x_min x_max y_min y_max fichero
./cod_07_06.py puntos.txt
./ej10_shamos_strong.py datos/ej_pts_01.txt
python3 pruebas.py
```

> [!warning] Errata en el enunciado
> El enunciado escribe `./cod_07_05.py 1000 2 0 10 0 10 puntos.txt`, pero el script **no recibe la dimensión** (la fija a 2). Con esa orden interpreta x ∈ [2, 0], y ∈ [10, 0] y escribe en un fichero llamado **`10`**. La orden correcta es `./cod_07_05.py 1000 0 10 0 10 puntos.txt`.
> Además, en `escribe_puntos` la línea `f.write('{0:g}\n'.format(p[-1]))` está *dentro* del bucle interior. En dimensión 2 da igual (el bucle da una sola vuelta), pero en dimensión ≥ 3 repetiría la última coordenada.

---

## Ejercicio 1: capitales europeas más próximas

Sin contar el Vaticano: **Viena y Bratislava**, a unos 55 km en línea recta.

Matiz (nota 2 del enunciado): sobre la Tierra la distancia correcta es la geodésica, no la euclídea sobre (latitud, longitud). El problema plano es solo una analogía.

## Ejercicios 2 y 3: fuerza bruta

Se recorren todas las parejas i < j y se guarda la mejor.

- Número de parejas: $\binom{n}{2} = \frac{n(n-1)}{2}$
- Cada distancia cuesta O(1)
- **Complejidad: Θ(n²)**. Recorre siempre todas las parejas, así que no hay caso mejor.

Comprobación empírica: al duplicar n, el tiempo se multiplica por unos ×4 (0,05 s → 0,20 s → 0,97 s con n = 1000, 2000, 4000).

## Ejercicio 4: ¿siempre existe x₀ con desigualdades estrictas?

**No.** Con `x < x₀` → P₁ y `x > x₀` → P₂, los puntos con x = x₀ no se asignan a ninguna parte.

- **Contraejemplo:** {(0, 0), (0, 1)}. Cualquier x₀ ≠ 0 deja los dos puntos en el mismo lado, y x₀ = 0 no asigna ninguno. Lo mismo pasa con cualquier nube en la que todos los puntos estén en una vertical.
- Los puntos generados por `cod_07_05.py` son distintos, pero **pueden compartir abscisa** (en `ej_pts_01.txt` hay 10 004 puntos y solo 6332 abscisas distintas).
- **Condición exacta:** con las abscisas ordenadas $x_{(1)} \le \dots \le x_{(n)}$, existe x₀ válido ⇔ $x_{(k)} < x_{(k+1)}$ para algún $k \in \{\lfloor n/2 \rfloor, \lceil n/2 \rceil\}$. En ese caso x₀ = punto medio, que es racional.

Por eso el ejercicio 5 relaja la condición a **≤ / ≥**: los puntos que están sobre la recta pueden ir a cualquiera de los dos lados.

## Ejercicio 5: partición en dos mitades

| Vía | Cómo | Coste |
|---|---|---|
| Ordenación | `sorted` por x y cortar en n//2 | **O(n log n)** |
| Mediana | x₀ = mediana; `<x₀` a P₁, `>x₀` a P₂; los `=x₀` rellenan P₁ hasta n//2 | **O(n)** si la mediana se calcula en O(n) |

> [!important] `statistics.median` NO es lineal
> Ordena la lista internamente: **O(n log n)**. Para tener O(n) hay que usar un algoritmo de selección: *quickselect* (O(n) esperado, que es el que está implementado) o *mediana de medianas* de Blum et al. (O(n) en el caso peor, el que cita Shamos).

Clave de la vía mediana: **repartir los empates** con x = x₀. Si van todos al mismo lado, las mitades quedan desequilibradas.

## Ejercicio 6: teorema maestro

$T(n) = 2T(n/2) + f(n)$ → $a = 2,\ b = 2,\ n^{\log_b a} = n$.

- **a)** f(n) = Θ(n) = Θ(n^{log_b a}) → caso 2 → **T(n) = Θ(n log n)**
- **b)** f(n) = Θ(n²) = Ω(n^{1+ε}) con ε = 1, y se cumple la regularidad: $2f(n/2) = n^2/2 \le c\,n^2$ con c = 1/2 → caso 3 → **T(n) = Θ(n²)**

**Conclusión:** si dividir y combinar cuesta más que lineal, el divide y vencerás **no mejora** a la fuerza bruta.

## Ejercicio 7: partición de una lista ya ordenada

Se corta por el índice n//2:
- los tamaños son n//2 y n − n//2,
- las dos mitades siguen ordenadas porque son trozos contiguos,
- x₀ = x del primer punto de X₂.

Coste O(n) por la copia (con índices sería O(1)). Exige un preproceso de ordenación de **una sola vez**, que cuesta O(n log n).

## Ejercicio 8: basta con mirar las bandas

**Enunciado.** Sea δ = mín(d(p₁,q₁), d(p₂,q₂)). Si p ∈ P₁, q ∈ P₂ y d(p, q) < δ, entonces p ∈ B₁ y q ∈ B₂.

**Demostración.** Como p ∈ P₁ y q ∈ P₂: $p_x \le x_0 \le q_x$. Entonces

$$d(p,q) = \sqrt{(q_x-p_x)^2 + (q_y-p_y)^2} \ \ge\ q_x - p_x = \underbrace{(x_0 - p_x)}_{\ge 0} + \underbrace{(q_x - x_0)}_{\ge 0}$$

Si d(p, q) < δ, cada sumando es < δ:
- $x_0 - p_x < \delta \Rightarrow x_0 - \delta < p_x \le x_0 \Rightarrow p \in B_1$
- $q_x - x_0 < \delta \Rightarrow x_0 \le q_x < x_0 + \delta \Rightarrow q \in B_2$

Por contrarrecíproco, cualquier pareja mixta fuera de las bandas cumple d(p, q) ≥ δ y se puede descartar. ∎

## Ejercicio 9: D&V con fuerza bruta en las bandas

Es correcto, pero **sigue siendo Θ(n²) en el peor caso**: si todos los puntos caen en las bandas, combinar cuesta |B₁|·|B₂|.

Resultado con `ej_pts_01.txt` (n = 10 004):
- **d((0, 0), (0, 2)) = 2**
- **49 987 284** parejas mixtas comprobadas ≈ n²/2, y unos 6–7 s, prácticamente lo mismo que la fuerza bruta.

El fichero está diseñado para esto: los 4 puntos (0,0), (0,2), (20,0), (20,2) fuerzan δ = 2, y los 10 000 restantes tienen x ≈ 10 (justo en la divisoria) con una separación vertical de 10. Todos caen en la banda, pero están **muy dispersos**, que es justo lo que aprovecha el ejercicio 10.

## Ejercicio 10: algoritmo de Shamos y Strong

**Preproceso** (O(n log n), una vez): X = puntos ordenados por x; Y = los mismos puntos ordenados por y. Cada punto lleva una **etiqueta** (su índice en la entrada).

**Paso recursivo:**

| Paso | Qué | Coste |
|---|---|---|
| a | X → X₁, X₂ cortando por la mitad | O(n) |
| b | Y → Y₁, Y₂ **filtrando** por etiqueta (se conserva el orden por y) | O(n) |
| c | Recursión → δ | 2T(n/2) |
| d | B₁ = puntos de Y₁ con x > x₀−δ; B₂ = puntos de Y₂ con x < x₀+δ | O(n) |
| e | Recorrido con dos índices, 5 candidatos por punto | O(n) |

$T(n) = 2T(n/2) + \Theta(n) \Rightarrow$ **Θ(n log n)** (más el preproceso, también O(n log n)).

**¿Por qué el paso (e) es lineal?**
- Fijado p ∈ B₁, sus posibles parejas están en el rectángulo $[x_0, x_0+\delta) \times (p_y-\delta, p_y+\delta)$, y ahí caben **como mucho 5** puntos de P₂, porque dos puntos de P₂ están a distancia ≥ δ entre sí.
- El índice j **nunca retrocede**: los p van subiendo, así que un q que ya está "demasiado abajo" para p también lo está para los siguientes.
- i recorre B₁ una vez y j recorre B₂ una vez, más 5 comparaciones por cada i → O(|B₁| + |B₂|).

> [!warning] Detalles que hay que cuidar
> - **Errata en (d):** el enunciado dice «puntos de **ordenada** mayor que x₀ − δ». Debe ser **abscisa**: la banda se define por x, aunque la lista esté ordenada por y.
> - **Pseudocódigo:** `while B2[j][1] ≤ ...` accede a B₂[j] antes de comprobar `j < |B2|`. Hay que poner `j < len(B2) and ...` **dentro** del while.
> - **Empates en x = x₀ al dividir Y:** si se decide el lado con `x < x₀`, un punto con x = x₀ puede acabar en Y₁ sin estar en X₁. Por eso se filtra por **etiqueta**, que además resuelve el caso de los puntos repetidos.
> - Si δ = 0 (hay puntos repetidos) se puede devolver la solución directamente.

**Resultados:** `ej_pts_01.txt` → d = 2 en **0,07 s** (frente a ~7 s del ejercicio 9). Al duplicar n, el tiempo se multiplica por algo más de ×2: 0,04 s → 0,09 s con n = 8000 → 16 000, y 100 000 puntos en < 1 s.

## Ejercicio 11: variante de Cormen

- Una **única franja** Y′ = puntos de Y con |x − x₀| < δ, ordenada por y.
- Cada punto se compara con los **5 siguientes** de Y′, sin mirar de qué lado son.
- Es correcto porque una pareja que mejore δ tiene que tener un punto en cada lado: dos puntos del mismo lado distan ≥ δ por definición de δ.
- Misma complejidad, **Θ(n log n)**, y código más simple (sin los dos índices i, j).

## Cota inferior (teoría)

- Ordenar por comparaciones: el árbol de decisión tiene n! hojas, así que su profundidad es ≥ log₂ n! = Θ(n log n).
- *Element uniqueness* (¿hay repetidos?) es Ω(n log n) con comparaciones de funciones lineales, y **se reduce** a la pareja más próxima en 1D: hay un repetido ⇔ la distancia mínima es 0.
- ⇒ Shamos–Strong es **asintóticamente óptimo** en ese modelo. Fuera de él: Rabin (probabilista, O(n)), Fortune–Hopcroft (determinista, O(n log log n)).

## Ejercicio 12: la pareja más distante (diámetro)

- **Fuerza bruta:** Θ(n²).
- **Algoritmo eficiente: Θ(n log n).**
  1. La pareja más distante está siempre entre los **vértices de la envolvente convexa**. Si un extremo fuera interior, se podría alejar más dentro del conjunto.
  2. Envolvente convexa (Graham o *Andrew monotone chain*): O(n log n).
  3. *Rotating calipers* sobre los h vértices de la envolvente: O(h) ⊆ O(n).
- **Cota inferior:** Ω(n log n) en el modelo de árboles de decisión algebraicos (Preparata–Shamos, por reducción desde la disyunción de conjuntos). Por tanto, el algoritmo anterior es óptimo.
- **Contraste interesante:** en dimensión 1 la pareja más distante es **O(n)** (mínimo y máximo), mientras que la más próxima en 1D sigue siendo Ω(n log n). La proximidad es "más difícil" que la lejanía.

## Para el examen

- [ ] Saber escribir la recurrencia y aplicar el teorema maestro en los dos casos
- [ ] Saber demostrar la restricción a las bandas (ejercicio 8)
- [ ] Explicar por qué bastan **5 candidatos** y por qué j no retrocede
- [ ] Justificar por qué el preproceso (X e Y) no empeora el coste
- [ ] `statistics.median` es O(n log n); la mediana lineal necesita un algoritmo de selección
- [ ] Reducción desde *element uniqueness* → cota Ω(n log n)
