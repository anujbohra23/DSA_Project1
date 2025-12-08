'''
This is the main script to run TSP experiments and generate plots.
'''

import os
from experiments import run_experiments
from plots import plot_runtime_vs_n, plot_approx_ratio_vs_n


def main():
    base_results_dir = "results"
    tables_dir = os.path.join(base_results_dir, "tables")
    plots_dir = os.path.join(base_results_dir, "plots")

    # 1. Run experiments
    print("[INFO] Running experiments...")
    df = run_experiments(
        ns_small=[6, 8, 10],
        ns_medium=[20, 50, 100, 200],
        trials=10,
        base_results_dir=base_results_dir,
        base_seed=123,
    )

    results_csv = os.path.join(tables_dir, "results.csv")

    # 2. Generate plots
    print("[INFO] Generating plots...")
    runtime_plot_path = os.path.join(plots_dir, "runtime_vs_n.png")
    approx_plot_path = os.path.join(plots_dir, "approx_ratio_vs_n.png")

    plot_runtime_vs_n(results_csv, runtime_plot_path)
    plot_approx_ratio_vs_n(results_csv, approx_plot_path)

    # 3. Print a quick summary
    print("\n[SUMMARY] Average tour length and runtime by n and method:")
    summary = df.groupby(["n", "method"]).agg(
        avg_length=("length", "mean"),
        avg_time=("time", "mean"),
    )
    print(summary)


if __name__ == "__main__":
    main()
