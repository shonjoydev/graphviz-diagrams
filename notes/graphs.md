# Graphs (Graphviz)

Graphs use fixed node positions, so every step of an algorithm keeps the same layout. The source files are in [`diagrams/dot/`](../diagrams/dot), and GitHub Actions renders them to [`diagrams/svg/`](../diagrams/svg).

## Weighted undirected graph

![Weighted graph](../diagrams/svg/graph-light.svg#gh-light-mode-only)
![Weighted graph](../diagrams/svg/graph-dark.svg#gh-dark-mode-only)

Source: [`graph-light.dot`](../diagrams/dot/graph-light.dot) · [`graph-dark.dot`](../diagrams/dot/graph-dark.dot)

## Minimum spanning tree (Kruskal / Prim)

![Minimum spanning tree](../diagrams/svg/mst-light.svg#gh-light-mode-only)
![Minimum spanning tree](../diagrams/svg/mst-dark.svg#gh-dark-mode-only)

Source: [`mst-light.dot`](../diagrams/dot/mst-light.dot) · [`mst-dark.dot`](../diagrams/dot/mst-dark.dot)

MST edges: `A–D (5)`, `B–E (5)`, `D–F (6)`, `A–C (7)`, `C–E (7)`, `E–G (9)`. Total weight: **39**.

### Kruskal's algorithm on this graph

| Step | Edge | Weight | Action |
|---|---|---|---|
| 1 | A–D | 5 | Add |
| 2 | B–E | 5 | Add |
| 3 | D–F | 6 | Add |
| 4 | A–C | 7 | Add |
| 5 | C–E | 7 | Add (joins {A,C,D,F} with {B,E}) |
| 6 | B–C | 8 | Skip (cycle) |
| 7 | E–F | 8 | Skip (cycle) |
| 8 | C–D | 9 | Skip (cycle) |
| 9 | E–G | 9 | Add (connects G) |

All 7 nodes are connected with 6 edges, so the algorithm stops.
