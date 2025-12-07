import itertools
from utils import tour_length

'''
Brute force approach for tsp solver. This will fix city 0 as the starting point, to avoid counting 
same tours with different rotations many times. A permutation of cities 1 to n-1 is gonna be gnerated
and each one will be used to find the tour length
Tour length and best tour will be returend here. 
'''

def brute_force_tsp(dist):
    n = len(dist)
    cities = list(range(n))
    best_tour = None
    best_len = float("inf")

    for perm in itertools.permutations(cities[1:]):
        tour = [0] + list(perm)
        length = tour_length(tour, dist)
        if length < best_len:
            best_len = length
            best_tour = tour

    return best_tour, best_len


