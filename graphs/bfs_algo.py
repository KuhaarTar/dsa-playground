from collections import deque


def bfs(graph, start, end):
    queue = deque(start)
    visited = [start]
    while queue:
        current = queue.popleft()
        if end == current:
            return True
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.append(neighbor)

    return False


def main():
    graph = {
        '5': ['3', '7'],
        '3': ['2', '4'],
        '7': ['8'],
        '2': [],
        '4': ['8'],
        '8': []
    }

    print(bfs(graph, '8', '5'))


if __name__ == "__main__":
    main()
