import heapq


def kruskal(graph, starting_vertex):
    mst = dict(set)
    visited = {starting_vertex}
    edges = [
        (cost, starting_vertex, to)
        for to, cost in graph[starting_vertex].items()
    ]
    heapq.heapify(edges)

    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst[frm].add(to)
            for to_next, cost2 in graph[to].items():
                if to_next not in visited:
                    heapq.heappush(edges, (cost2, to, to_next))

    return mst
