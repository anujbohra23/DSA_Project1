---

Travelling Salesperson Problem (TSP) — Approximation & Heuristic Algorithms
CS 512 – Final Project

---

## Project Overview

The Travelling Salesperson Problem (TSP) asks:
*Given a set of cities and pairwise distances, find the shortest tour that visits each city once and returns to the start.*

TSP is NP-hard, and exact solutions scale factorially. This project explores the performance of approximation and heuristic algorithms including:

* Brute Force (optimal, for small n)
* Nearest Neighbor (greedy heuristic)
* 2-Opt (local search refinement)

The project compares algorithms by runtime, tour quality, and approximation ratio.

---

## Project Structure

```
tsp_project/
│
├── main.py
├── utils.py
├── brute_force.py
├── nearest_neighbor.py
├── two_opt.py
├── experiments.py
├── plots.py
│
├── results/
│   ├── tables/results.csv
│   └── plots/
│
└── requirements.txt
```

---

## Installation

```
pip install -r requirements.txt
```

(Optional)

```
python3 -m venv venv
source venv/bin/activate     # Mac/Linux
venv\Scripts\activate        # Windows
```

---

## Running the Project

```
python main.py
```

This will:

* Generate random TSP datasets
* Run Brute Force, Nearest Neighbor, and 2-Opt
* Save results to `results/tables/results.csv`
* Generate:

  * `runtime_vs_n.png`
  * `approx_ratio_vs_n.png`
  * Example tour visualizations for each n

---

## Summary of Observations

* Brute Force is feasible only for n ≤ 10 (factorial growth).
* Nearest Neighbor runs fast and scales well but may produce suboptimal tours.
* 2-Opt significantly improves NN tours but has higher computational cost.
* Approximation ratios show NN is ~1–2% worse than optimal; 2-Opt improves to ~0.5–1.3%.

---

## Algorithms Implemented

**Brute Force (O(n!))**
Enumerates all tours to obtain the optimal route.

**Nearest Neighbor (O(n²))**
Constructs a greedy tour by repeatedly choosing the closest unvisited city.

**2-Opt (≈O(n³))**
Local search technique that improves a tour by reversing edges to reduce crossings.

---

## Outputs

* Average runtimes per algorithm
* Approximation ratios for small n
* Visual tour diagrams (optimal vs heuristic)
* CSV logs of all experimental results

---

## References

* Gutin & Punnen (2002), *The Traveling Salesman Problem and Its Variations*
* TSPLIB benchmark dataset archive

---