def dfs(graph, current_node, visited, stack):
    visited.append(current_node)

    for current in graph[current_node]:
        if current not in visited:
            dfs(graph, current, visited, stack)

    stack.append(current_node)


def topological_sort(graph):
    visited = [node for node in graph if not graph[node]]
    stak = []
    for curr in graph:
        if curr not in visited:
            dfs(graph, curr, visited, stak)

    return stak[::-1]


def main():
    graph = {'0': {'1', '2'},
             '1': {'0', '3', '4'},
             '2': {'0'},
             '3': {'1'},
             '4': {'2', '3'}}
    print(topological_sort(graph))


if __name__ == "__main__":
    main()
