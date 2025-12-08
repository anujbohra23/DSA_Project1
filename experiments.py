'''
This will run experiments comparing TSP algorithms on small and medium instances.
For small instances, it computes the optimal solution via brute-force search
and compares it to heuristic methods (Nearest Neighbor and 2-Opt). For medium
instances, it runs only the heuristics due to computational constraints.
Results are saved in CSV format along with example plots of tours.
'''

import os
import time
import random
import pandas as pd

from utils import (
    set_global_seed,
    generate_random_cities,
    build_distance_matrix,
    plot_tour,
)
from brute_force import brute_force_tsp
from nearest_neighbor import best_of_all_starts
from two_opt import two_opt


def run_experiments(
    ns_small=None,
    ns_medium=None,
    trials: int = 10,
    base_results_dir: str = "results",
    base_seed: int = 123,
):
    if ns_small is None:
        ns_small = [6, 8, 10]
    if ns_medium is None:
        ns_medium = [20, 50, 100, 200]

    tables_dir = os.path.join(base_results_dir, "tables")
    plots_dir = os.path.join(base_results_dir, "plots")
    os.makedirs(tables_dir, exist_ok=True)
    os.makedirs(plots_dir, exist_ok=True)

    rows = []

    # SMALL n: compare to optimal
    for n in ns_small:
        for trial_idx in range(trials):
            # For reproducibility, vary seed based on n and trial
            seed = base_seed + n * 1000 + trial_idx
            set_global_seed(seed)

            cities = generate_random_cities(n)
            dist = build_distance_matrix(cities)

            # Brute-force optimal
            t0 = time.perf_counter()
            opt_tour, opt_len = brute_force_tsp(dist)
            t1 = time.perf_counter()
            opt_time = t1 - t0

            rows.append(
                {
                    "n": n,
                    "trial": trial_idx,
                    "method": "optimal",
                    "length": opt_len,
                    "time": opt_time,
                    "approx_ratio": 1.0,
                }
            )

            # Nearest Neighbor (best of all starts)
            t0 = time.perf_counter()
            nn_tour, nn_len = best_of_all_starts(dist)
            t1 = time.perf_counter()
            nn_time = t1 - t0

            rows.append(
                {
                    "n": n,
                    "trial": trial_idx,
                    "method": "nearest_neighbor",
                    "length": nn_len,
                    "time": nn_time,
                    "approx_ratio": nn_len / opt_len,
                }
            )

            # 2-Opt starting from NN tour
            t0 = time.perf_counter()
            two_opt_tour, two_opt_len = two_opt(dist, nn_tour)
            t1 = time.perf_counter()
            two_opt_time = t1 - t0

            rows.append(
                {
                    "n": n,
                    "trial": trial_idx,
                    "method": "two_opt",
                    "length": two_opt_len,
                    "time": two_opt_time,
                    "approx_ratio": two_opt_len / opt_len,
                }
            )

            # For the first small instance of each n, save a visual example
            if trial_idx == 0:
                opt_plot_path = os.path.join(
                    plots_dir, f"example_n{n}_optimal.png"
                )
                nn_plot_path = os.path.join(
                    plots_dir, f"example_n{n}_nn.png"
                )
                two_opt_plot_path = os.path.join(
                    plots_dir, f"example_n{n}_two_opt.png"
                )

                plot_tour(
                    cities, opt_tour, opt_plot_path, title=f"Optimal Tour (n={n})"
                )
                plot_tour(
                    cities,
                    nn_tour,
                    nn_plot_path,
                    title=f"Nearest Neighbor Tour (n={n})",
                )
                plot_tour(
                    cities,
                    two_opt_tour,
                    two_opt_plot_path,
                    title=f"2-Opt Tour (n={n})",
                )

    # MEDIUM n: only heuristics, no ground truth
    for n in ns_medium:
        for trial_idx in range(trials):
            seed = base_seed + n * 1000 + trial_idx
            set_global_seed(seed)

            cities = generate_random_cities(n)
            dist = build_distance_matrix(cities)

            # Nearest Neighbor
            t0 = time.perf_counter()
            nn_tour, nn_len = best_of_all_starts(dist)
            t1 = time.perf_counter()
            nn_time = t1 - t0

            rows.append(
                {
                    "n": n,
                    "trial": trial_idx,
                    "method": "nearest_neighbor",
                    "length": nn_len,
                    "time": nn_time,
                    "approx_ratio": None,
                }
            )

            # 2-Opt
            t0 = time.perf_counter()
            two_opt_tour, two_opt_len = two_opt(dist, nn_tour)
            t1 = time.perf_counter()
            two_opt_time = t1 - t0

            rows.append(
                {
                    "n": n,
                    "trial": trial_idx,
                    "method": "two_opt",
                    "length": two_opt_len,
                    "time": two_opt_time,
                    "approx_ratio": None,
                }
            )

            # For the first trial of each medium n, save a visual example
            if trial_idx == 0:
                nn_plot_path = os.path.join(
                    plots_dir, f"example_n{n}_nn.png"
                )
                two_opt_plot_path = os.path.join(
                    plots_dir, f"example_n{n}_two_opt.png"
                )

                plot_tour(
                    cities,
                    nn_tour,
                    nn_plot_path,
                    title=f"Nearest Neighbor Tour (n={n})",
                )
                plot_tour(
                    cities,
                    two_opt_tour,
                    two_opt_plot_path,
                    title=f"2-Opt Tour (n={n})",
                )

    df = pd.DataFrame(rows)
    results_csv_path = os.path.join(tables_dir, "results.csv")
    df.to_csv(results_csv_path, index=False)
    print(f"[INFO] Saved experiment results to: {results_csv_path}")
    return df
