from utils import tour_length
'''
2-Opt local search algorithm for TSP. It takes an initial tour and tries to improve it 
by swapping two edges at a time. Done until there is no improvement. 
'''

def two_opt_swap(tour, i, k):
    return tour[:i] + tour[i : k + 1][::-1] + tour[k + 1 :]


def two_opt(dist, initial_tour):
    tour = initial_tour[:]
    best_length = tour_length(tour, dist)
    n = len(tour)

    improved = True
    while improved:
        improved = False
        # we will keep the first and last city fixed (0)
        for i in range(1, n - 2):
            for k in range(i + 1, n - 1):
                new_tour = two_opt_swap(tour, i, k)
                new_length = tour_length(new_tour, dist)
                if new_length < best_length:
                    tour = new_tour
                    best_length = new_length
                    improved = True
                    break
            if improved:
                break

    return tour, best_length
