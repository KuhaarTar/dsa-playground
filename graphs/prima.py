def prims_algorithm(graph):
    vertices = list(graph.keys())
    N = len(vertices)
    selected_node = [0] * N
    selected_node[0] = True
    edges_count = 0
    min_spanning_tree = []

    while edges_count < N - 1:
        minimum = float('inf')
        x = 0
        y = 0
        for i in range(N):
            for neighbor, weight in graph[vertices[i]].items():
                j = vertices.index(neighbor)
                if (not selected_node[j]) and weight:
                    if minimum > weight:
                        minimum = weight
                        x = i
                        y = j

        min_spanning_tree.append((vertices[x], vertices[y], graph[vertices[x]][vertices[y]]))
        selected_node[y] = True
        edges_count += 1

    return min_spanning_tree


def main():
    graph_ = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

    minimum_spanning_tree = prims_algorithm(graph_)
    print("Minimum Spanning Tree:")
    print(minimum_spanning_tree)
    for edge in minimum_spanning_tree:
        print(f"{edge[0]} - {edge[1]} : {edge[2]}")


if __name__ == "__main__":
    main()
