def dfs(graph: {str: {str}}, current_node: str, final_node: str, visited=[], path=[]) -> [str]:
    """
    Implement DFS algorithm
    :param graph: A graph is represented by a list of adjacencies
    :param current_node:
    :param final_node:
    :param visited:
    :param path: Array that contains path from start node to end node
    :return:
    """
    visited = [*visited, current_node]
    path = [*path, current_node]
    if current_node == final_node:
        return path
    for neighbor in graph[current_node]:
        if neighbor not in visited:
            path_ = dfs(graph, neighbor, final_node, visited, path)
            if path_:
                return path_


def main():
    graph = {'0': {'1', '2'},
             '1': {'0', '3', '4'},
             '2': {'0'},
             '3': {'1'},
             '4': {'2', '3'}}
    print(dfs(graph, '0', '2'))


if __name__ == "__main__":
    main()
