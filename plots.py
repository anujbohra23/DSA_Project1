import os
import pandas as pd
import matplotlib.pyplot as plt


def plot_runtime_vs_n(results_csv: str, out_path: str):
    """
    Plot average runtime vs n for each method.
    """
    df = pd.read_csv(results_csv)

    # group by n and method
    grouped = df.groupby(["n", "method"])["time"].mean().reset_index()

    plt.figure()
    methods = grouped["method"].unique()
    for method in methods:
        subset = grouped[grouped["method"] == method]
        plt.plot(subset["n"], subset["time"], marker="o", label=method)

    plt.xlabel("Number of cities (n)")
    plt.ylabel("Average runtime (seconds)")
    plt.title("Runtime vs n")
    plt.legend()
    plt.tight_layout()
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    plt.savefig(out_path)
    plt.close()
    print(f"[INFO] Saved runtime plot to: {out_path}")


def plot_approx_ratio_vs_n(results_csv: str, out_path: str):
    """
    Plot average approximation ratio vs n for heuristic methods.
    Uses only rows where approx_ratio is not NaN (i.e., small n with optimal).
    """
    df = pd.read_csv(results_csv)

    df = df[df["approx_ratio"].notna()]
    # remove "optimal" since its ratio is 1 by definition
    df = df[df["method"] != "optimal"]

    grouped = df.groupby(["n", "method"])["approx_ratio"].mean().reset_index()

    plt.figure()
    methods = grouped["method"].unique()
    for method in methods:
        subset = grouped[grouped["method"] == method]
        plt.plot(subset["n"], subset["approx_ratio"], marker="o", label=method)

    plt.xlabel("Number of cities (n)")
    plt.ylabel("Average approximation ratio")
    plt.title("Approximation Ratio vs n")
    plt.legend()
    plt.tight_layout()
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    plt.savefig(out_path)
    plt.close()
    print(f"[INFO] Saved approximation ratio plot to: {out_path}")
