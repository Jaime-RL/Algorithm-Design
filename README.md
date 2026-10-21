# Algorithm Design

Algorithm design techniques implemented in Python: **exhaustive generation**, **greedy strategies**, **backtracking** and **branch & bound** applied to combinatorial problems.

> 🚧 Work in progress — new exercises are added as the course advances.

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

## Running

```bash
cd backtracking
python 04_cod_02.py 04_dat_01.txt          # greedy solution
python 04_cod_08.py 04_dat_02.txt          # optimal solution with branch & bound
python 04_cod_09.py 30 40 my_instance.txt  # random instance: 30 candidates, 40 skills
```

The modules load each other with `importlib` because their file names start with a digit, so run them from inside their folder.

## Tech

Python 3 (standard library only)
