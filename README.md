# Constructions of fullerenes that maximize the anionic Clar number.

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

The code in this repo generates the adjacency lists of fullerenes defined
by the constructions in [INSERT PAPER]. These fullerenes are used to prove
tight upper bounds for the $p$-anionic Clar number of fullerenes on $n$ vertices
(for even $p > 0$).

**NOTE:** There are other fullerenes that maximize the $p$-anionic Clar
numbers on $n$ vertices, the fullerenes generated here are simply
those defined by the constructions in [INSERT PAPER].

### Requirements:

A Python library that can call `import sys`

### Files:

There are seven files used to generate fullerenes:

`build/02_make_adj.py` <- Fullerenes that maximize $C_2(F_n)$ on $n \ge 40$ ($n
\neq 40$) vertices.

`build/04_make_adj.py` <- Fullerenes that maximize $C_4(F_n)$ on $n \ge 36$ ($n
\neq 40$) vertices.

`build/06_make_adj.py` <- Fullerenes that maximize $C_6(F_n)$ on $n \ge 56$
vertices.

`build/08_make_adj.py` <- Fullerenes that maximize $C_8(F_n)$ on $n \ge 58$
vertices.

`build/10_make_adj.py` <- Fullerenes that maximize $C_{10}(F_n)$ on $n \ge 54$
($n \neq 58$) vertices.

`build/12_2_mod_6_make_adj.py` <- Fullerenes that maximize $C_{12}(F_n)$ on $n
\ge 110$ ($n \equiv 2 \mod{6}$) vertices.

`build/12_4_mod_6_make_adj.py` <- Fullerenes that maximize $C_{12}(F_n)$ on $n
= 70$ and $n \ge 88$ ($n \equiv 4 \mod{6}$) vertices.

**Note:** Leapfrog fullerenes maximize the 12-anionic Clar number
$n \equiv 0 \mod{6}$ vertices.

### To run:

`python {file you want to run} {n}`

where `n` is the maximum size of a fullerene you would like to generate.

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
  author =        {Slobodin, A.},
  month =         sep,
  title =         {{Constructions of fullerenes that maximize the
                   anionic Clar number}},
  year =          {2024},
  url =           {https://github.com/fastbodin/
                  anionic_clar_fullerene_construction},
}
```
