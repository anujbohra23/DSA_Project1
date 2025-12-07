import csv
import math
import os
import random
import matplotlib.pyplot as plt

''''
this contains functions for creating cities saving them to csv and loading them'''

def set_global_seed(seed: int = 42) -> None: # we will use the random seed
    random.seed(seed)


def generate_random_cities(n: int, width: float = 100.0, height: float = 100.0):
    """
    n random cities with coordinates in [0, width] x [0, height]. it returns 
    a list of city id and their cordinates as (city_id, x, y)
    """
    cities = []
    for i in range(n):
        x = random.uniform(0.0, width)
        y = random.uniform(0.0, height)
        cities.append((i, x, y))
    return cities


def save_cities_to_csv(cities, path: str) -> None:
    """
    saving these cities in csv        
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "x", "y"])
        for city_id, x, y in cities:
            writer.writerow([city_id, x, y])


def load_cities_from_csv(path: str):
    """
    loading cities to use in diff methods
    """
    cities = []
    with open(path, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            city_id = int(row["id"])
            x = float(row["x"])
            y = float(row["y"])
            cities.append((city_id, x, y))
    return cities


def euclidean_distance(city1, city2) -> float:
    _, x1, y1 = city1
    _, x2, y2 = city2
    return math.hypot(x1 - x2, y1 - y2)


def build_distance_matrix(cities):
    """
    dist[i][j] = Euclidean distance between city i and j.
    cities are in a list indexed by city_id.
    """
    n = len(cities)
    dist = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            d = euclidean_distance(cities[i], cities[j])
            dist[i][j] = d
            dist[j][i] = d
    return dist


def tour_length(tour, dist) -> float:
    """
    total length of a tour based on the distance matrix.
    tour is a list of city indices and dist is the distance matrix
    """
    total = 0.0
    n = len(tour)
    for i in range(n):
        a = tour[i]
        b = tour[(i + 1) % n] 
    return total


def plot_tour(cities, tour, out_path: str, title: str = "TSP Tour"):
    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    xs = [cities[i][1] for i in tour] + [cities[tour[0]][1]]
    ys = [cities[i][2] for i in tour] + [cities[tour[0]][2]]

    plt.figure()
    plt.scatter(xs, ys)
    plt.plot(xs, ys)

    # annotate city with city id
    for city_id, x, y in cities:
        plt.text(x, y, str(city_id))

    plt.title(title)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()
