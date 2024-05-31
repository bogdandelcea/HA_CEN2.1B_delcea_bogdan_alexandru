import heapq

def tsp_ucs(graph):
    cities = list(graph.keys())
    start = cities[0]
    pq = [(0, start, [start])]
    min_longest_dist = float('inf')
    best_route = None

    while pq:
        current_cost, current_city, path = heapq.heappop(pq)
        if len(path) == len(cities) and path[0] == start:
            if current_cost < min_longest_dist:
                min_longest_dist = current_cost
                best_route = path
        else:
            for next_city in cities:
                if next_city not in path or (len(path) == len(cities) and next_city == start):
                    new_cost = max(current_cost, graph[current_city][next_city])
                    new_path = path + [next_city]
                    heapq.heappush(pq, (new_cost, next_city, new_path))

    return best_route, min_longest_dist

# Example graph
graph = {
    'A': {'A': 0, 'B': 1, 'C': 4, 'D': 7},
    'B': {'A': 1, 'B': 0, 'C': 2, 'D': 8},
    'C': {'A': 4, 'B': 2, 'C': 0, 'D': 3},
    'D': {'A': 7, 'B': 8, 'C': 3, 'D': 0}
}

graph_1 = {
    'A': {'A': 0, 'B': 2, 'C': 5, 'D': 3, 'E': 6},
    'B': {'A': 2, 'B': 0, 'C': 4, 'D': 7, 'E': 2},
    'C': {'A': 5, 'B': 4, 'C': 0, 'D': 8, 'E': 3},
    'D': {'A': 3, 'B': 7, 'C': 8, 'D': 0, 'E': 5},
    'E': {'A': 6, 'B': 2, 'C': 3, 'D': 5, 'E': 0}
}


graph_2 = {
    'A': {'A': 0, 'B': 3, 'C': 6, 'D': 9, 'E': 12},
    'B': {'A': 3, 'B': 0, 'C': 5, 'D': 8, 'E': 11},
    'C': {'A': 6, 'B': 5, 'C': 0, 'D': 7, 'E': 10},
    'D': {'A': 9, 'B': 8, 'C': 7, 'D': 0, 'E': 9},
    'E': {'A': 12, 'B': 11, 'C': 10, 'D': 9, 'E': 0}
}

route, cost = tsp_ucs(graph_2)
print(f"Best route (UCS): {route} with cost: {cost}")
