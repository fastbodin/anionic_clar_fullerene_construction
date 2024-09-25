# Constructions of fullerenes that maximize the $p$-anionic Clar number for $p
> 0$.

## Background

A **fullerene** $F_n$ is a 3-regular graph such that every face is a pentagon
or a hexagon. By Euler's formula, there are exactly 12 pentagons. Let $F(F_n)$
and $E(F_n)$ denote the set of faces and edges in a fullerene $F_n$,
respectively. For a fixed integer p, a **p-anionic resonance structure**
$(\mathcal{F}, \mathcal{M})$ of a fullerene $F_n$ is a set of independent faces
$\mathcal{F} \subseteq F(F_n)$ (containing exactly p pentagons) and a perfect
matching $\mathcal{M} \subseteq E(F_n)$ on the graph obtained from $F_n$ by
removing the vertices of the faces in $\mathcal{F}$. The **p-anionic Clar
number** $C_p(F_n)$ of a fullerene $F_n$ is defined to be zero if $F_n$ has no
p-anionic resonance structures and, otherwise, to be equal to the maximum value
of $|\mathcal{F}|$ over all p-anionic resonance structures $(\mathcal{F},
\mathcal{M})$ of $F_n$. A p-anionic resonance structure that has $C_p(F_n)$
faces in $\mathcal{F}$ is called a **p-anionic Clar structure** on $F_n$.

## Code

### Requirements:

1. A Python library that can call `import sys`

### Files:
There are seven files used to generate fullerenes:

`02_make_adj.py` <- Generates fullerenes that maximize the 2-anionic Clar number
on $n \ge 40$ (except for $n = 40$) vertices.

`04_make_adj.py` <- Generates fullerenes that maximize the 4-anionic Clar number
on $n \ge 36$ (except for $n = 40$) vertices.

`06_make_adj.py` <- Generates fullerenes that maximize the 6-anionic Clar number
on $n \ge 56$ vertices.

`08_make_adj.py` <- Generates fullerenes that maximize the 8-anionic Clar number
on $n \ge 58$ vertices.

`10_make_adj.py` <- Generates fullerenes that maximize the 10-anionic Clar number
on $n \ge 54$ (except for $n = 58$) vertices.

`12_2_mod_6_make_adj.py` <- Generates fullerenes that maximize the 12-anionic Clar
number on $n \ge 110$ vertices where $n$ is congruent to 2 modulo 6

`12_4_mod_6_make_adj.py` <- Generates fullerenes that maximize the 12-anionic Clar
number on $n \ge 88$ vertices where $n$ is congruent to 4 modulo 6

Note that leapfrog fullerenes maximize the 12-anionic Clar number on $n$
vertices when $n$ is congruent to $0$ modulo $6$.

### To run:
`{file you want to run}.py {n}` where `n` is the maximum size of a
fullerene you would like to generate.

### Output:
The adjacency lists of fullerenes that maximize the chosen $p$-anionic
Clar number with the following format:

```
{number of vertices in graph (call it n)}
{degree of vertex 0} {neighbor 0} {neighbor 1} {neighbor 2}
{degree of vertex 1} {neighbor 0} {neighbor 1} {neighbor 2}
...
{degree of vertex n-1} {neighbor 0} {neighbor 1} {neighbor 2}
```

Such that **there exists a planar embedding of the vertices where each neighbor
is listed in clockwise order.**

**NOTE:** The constructions implemented in the code do not necessarily
construct unique fullerenes. To check that two fullerenes on $n$ vertices
(with the output adjacency lists) are unique, you need to check that there
is no automorphism between the two.

## Citation

If you use this code in your research, please cite it via:

```
@software{Slobodin_Constructions_of_fullerenes_2024,
author = {Slobodin, A.},
month = sep,
title = {{Constructions of fullerenes that maximize the $p$-anionic Clar number for $p > 0$.}},
url = {https://github.com/fastbodin/anionic_clar_fullerene_construction},
version = {1.0.0},
year = {2024}
}
```
