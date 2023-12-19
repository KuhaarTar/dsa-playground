def bellman_ford(graph: {str: {str: int}}, start: str):
    dist_to = {node: float("inf") for node in graph}
    dist_to[start] = 0
    n = len(graph) - 1

    for _ in range(n):
        for current in graph:
            for neighbor, weight in graph[current].items():
                new_dist = dist_to[current] + weight
                if dist_to[neighbor] > new_dist:
                    dist_to[neighbor] = new_dist

    for current in graph:
        for neighbor, weight in graph[current].items():
            new_dist = dist_to[current] + weight
            if dist_to[neighbor] > new_dist:
                raise ValueError("Negative cycle appear")

    return dist_to


graph_ = {
    'A': {'B': -1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': -1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
shortest_distances = bellman_ford(graph_, start_node)
print(f"Shortest distances from node {start_node}: {shortest_distances}")
