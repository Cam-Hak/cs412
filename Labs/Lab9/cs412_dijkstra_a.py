"""
name: Cameron Hakenson
"""

from queue import PriorityQueue


def dijkstras(n, edges, src):
    adj = {}

    for i in range(n):
        adj[i] = []

    for u, v, w in edges:
        adj[u].append([v, w])

    shortest = {}
    pq = PriorityQueue()
    pq.put((0, src))

    while not pq.empty():
        weight, edge = pq.get()
        if edge in shortest:
            continue

        shortest[edge] = weight
        for e, w in adj[edge]:
            if e not in shortest:
                pq.put((w + weight, e))

    return shortest


def main():
    data = input().split()
    n = int(data[0])
    m = int(data[1])
    q = int(data[2])

    edges = []
    querys = []

    for _ in range(m):
        edge = []
        edge_input = input().split()
        for e in edge_input:
            edge.append(int(e))

        edges.append(edge)

    for _ in range(q):
        query = []
        query_input = input().split()
        for e in query_input:
            query.append(int(e))

        querys.append(query)

    # used for testing
    # n = 4
    # edges = [[0, 1, 2], [1, 2, 2], [3, 0, 2]]
    # querys = [[0, 0], [0, 1], [0, 2], [0, 3]]

    for s, e in querys:
        path = dijkstras(n, edges, s)
        if e in path:
            print(path[e])
        else:
            print("Impossible")


if __name__ == "__main__":
    main()
