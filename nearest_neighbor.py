from utils import tour_length

"""
    Nearest Neighbor method, it builds the tour by visiting the closest unvisited 
    city for the salesman. and then returning to the start. It takes distance matrix
    as an input and the index of the starting city. It finally returns tour of the entire 
    grid and length of the tour as well just like brute force.
"""

def nearest_neighbor(dist, start: int = 0):
    n = len(dist)
    unvisited = set(range(n))
    unvisited.remove(start)
    tour = [start]
    current = start

    while unvisited:
        next_city = min(unvisited, key=lambda j: dist[current][j])
        unvisited.remove(next_city)
        tour.append(next_city)
        current = next_city

    length = tour_length(tour, dist)
    return tour, length


def best_of_all_starts(dist): #this finds the best tour by checking all
    n = len(dist)
    best_tour = None
    best_len = float("inf")

    for start in range(n):
        tour, length = nearest_neighbor(dist, start=start)
        if length < best_len:
            best_len = length
            best_tour = tour

    return best_tour, best_len

