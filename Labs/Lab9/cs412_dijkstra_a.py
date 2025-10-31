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
        edge, weight = pq.get()
        if edge in shortest:
            continue

        shortest[edge] = weight
        for e, w in adj[edge]:
            if e not in shortest:
                pq.put((w, e))

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

    print(dijkstras(n, edges, 0))


if __name__ == "__main__":
    main()
