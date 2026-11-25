# Algorithm Design

Algorithm design techniques implemented in Python: **exhaustive generation**, **greedy strategies**, **backtracking**, **branch & bound** and **divide & conquer**, plus Eulerian paths and Rabin-Karp string matching. Code comments are in Spanish.

## Contents

### `graphs/` — Exhaustive generation of graphs

| File | Description |
|---|---|
| `ej1.py` | Generates every undirected graph on *n* labelled vertices by enumerating the upper-triangular 0/1 adjacency matrices |
| `ej2.py` | Generates every directed graph on *n* labelled vertices (0/1 adjacency matrices with zero diagonal) |
| `ej3.py` | Generators for **unlabelled** graphs and digraphs: memoises already computed graphs and filters out isomorphic ones |

### `backtracking/` — The *set cover* problem

Given a set of people, each with a set of skills, choose the **smallest team that covers every required skill**.

| File | Description |
|---|---|
| `04_cod_03.py` | Partial-solution class for set cover (state, extension, completeness check) |
| `04_cod_07.py` | Extends the partial solution with a **greedy** expansion strategy |
| `04_cod_02.py` | Greedy solver built on top of the partial-solution classes |
| `04_cod_11.py` | Optimised partial solution with **pruning bounds** (counts of people per number of skills) |
| `04_cod_08.py` | **Branch & bound** search for the optimal team |
| `04_cod_09.py` | Random instance generator |
| `04_dat_0*.txt` | Sample input instances |

### `dyv/` — Closest pair of points (divide & conquer)

Given *n* points in the plane, find the two closest ones. From Θ(n²) brute force to the Θ(n log n) divide & conquer algorithm.

| File | Description |
|---|---|
| `puntos.py` | Shared helpers: read a points file, Euclidean distance, print the result |
| `cod_07_05.py` | Random generator of distinct points inside a rectangle |
| `cod_07_06.py` | **Brute force**: tries every pair, Θ(n²) |
| `ej05_particion.py` | Splits the points into two halves by x, either by sorting (O(n log n)) or with the median via quickselect (expected O(n)) |
| `ej07_particion_ordenada.py` | Splits a list already sorted by x at its middle index |
| `ej09_bandas.py` | Divide & conquer with brute force inside the two strips: correct but still Θ(n²) in the worst case |
| `ej10_shamos_strong.py` | **Shamos & Strong**: presorted X and Y lists and a linear combine step that checks 5 candidates per point, Θ(n log n) |
| `ej11_cormen.py` | **Cormen et al.** variant: a single strip sorted by y, each point compared with the next 5, Θ(n log n) |
| `pruebas.py` | Checks every algorithm against brute force (random clouds, grids, repeated and vertical points, the sample files) and times them |
| `ej_pts_0*.txt` | Sample inputs (`ej_pts_01.txt` is a worst case for `ej09_bandas.py`) |
| `Practica07_pareja_mas_proxima.md` | Notes on the assignment (in Spanish) |

### `konigsberg/` — Eulerian paths

| File | Description |
|---|---|
| `ejercicio5.py` | Is the (possibly disconnected) multigraph Eulerian? Edges must lie in one component and every degree must be even |
| `ejercicio6.py` | Does it have an Eulerian path? Returns `True` (cycle), the two endpoints, or `False` |
| `ejercicio7.py` | Builds the Eulerian path or cycle with **Hierholzer's algorithm** |
| `facultad.py` | Models the floors and staircases of a faculty building as a `MultiGraph` and answers whether every flight can be walked exactly once |
| `test_euleriano.py`, `test_camino.py` | pytest tests for exercises 5–7 |

### `patron.py` — String matching

`rabin_karp(t, p)` returns every position where pattern `p` occurs in text `t`, using a rolling hash and checking each hash match character by character.

## Running

```bash
cd backtracking
python 04_cod_02.py 04_dat_01.txt          # greedy solution
python 04_cod_08.py 04_dat_02.txt          # optimal solution with branch & bound
python 04_cod_09.py 30 40 my_instance.txt  # random instance: 30 candidates, 40 skills

cd ../dyv
python cod_07_05.py 1000 0 10 0 10 puntos.txt  # 1000 random points in [0,10]x[0,10]
python cod_07_06.py puntos.txt                  # brute force
python ej10_shamos_strong.py puntos.txt          # O(n log n)
python pruebas.py                               # correctness checks + timings

cd ../konigsberg
python facultad.py
pytest
```

Run each script from inside its folder: the modules import each other by file name (the `backtracking/` ones through `importlib`, because their names start with a digit).

## Tech

Python 3. `backtracking/`, `graphs/`, `dyv/` and `patron.py` use only the standard library; `konigsberg/` uses NetworkX, and its tests run with pytest.
