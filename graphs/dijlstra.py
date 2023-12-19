def dijkstra(graph: {str: {str: int}}, start: str):
    dist_to = {node: float("inf") for node in graph}
    dist_to[start] = 0
    visited = []
    while len(visited) < len(graph):
        current = min((node for node in dist_to if node not in visited),
                      key=lambda node: dist_to[node])
        visited.append(current)
        for neighbor, weight in graph[current].items():
            if neighbor not in visited:
                new_dist = dist_to[current] + weight
                if dist_to[neighbor] > new_dist:
                    dist_to[neighbor] = new_dist
    return dist_to

graph_ = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_vertex = 'A'
result = dijkstra(graph_, start_vertex)

print(f"Найкоротші відстані від вузла {start_vertex}: {result}")
