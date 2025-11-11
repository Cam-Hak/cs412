"""
CS 412 Lab: Maxflow and Min cut

Implement the Ford/Fulkerson augmenting-path algorithm for computing the
max flow of a graph.
"""

import queue


"""
Depth first search

Accepts a graph in an adjacency list (does not care about payload for edges)
Starts a traversal at s and stops when either there are no more vertices
to explore or it reaches vertex t.

Returns: list of predecesors/parents in the tree resulting from the DFS.
If vertex t is unreachable, it will not be in the returned dictionary
"""


def dfs(G, s, t):
    bag = queue.LifoQueue()
    bag.put((None, s))
    dfs_parents = {}
    while not bag.empty() and dfs_parents.get(t) is None:

        p, u = bag.get()

        if u not in dfs_parents:
            dfs_parents[u] = p
            for v in G[u]:
                bag.put((u, v))

    return dfs_parents


def main():
    vertex_count, edge_count = [int(x) for x in input().split()]

    adj_list = {}
    # create vertices numbered 0 to vertex_count - 1
    for i in range(vertex_count):
        adj_list[i] = {}

    # the value for each edge is a list.  First element is the flow,
    # second element is the capacity.

    for _ in range(edge_count):
        u, v, cap = [int(x) for x in input().split()]
        adj_list[u][v] = [0, cap]

    # print('adjlist', adj_list)

    # by the problem definition, define s and t as follows
    s = 0
    t = vertex_count - 1

    max_flow = 0

    while True:
        residual = {}
        for i in range(vertex_count):
            residual[i] = {}

        for u in adj_list:
            for v in adj_list[u]:
                flow, capacity = adj_list[u][v]
                if capacity - flow > 0:
                    residual[u][v] = capacity - flow
                if flow > 0:
                    residual[v][u] = flow

        parents = dfs(residual, s, t)

        if t not in parents:
            break

        path = []
        current = t
        while current != s:
            parent = parents[current]
            path.append((parent, current))
            current = parent
        path.reverse()

        bottleneck = float("inf")
        for u, v in path:
            bottleneck = min(bottleneck, residual[u][v])

        for u, v in path:
            if v in adj_list[u]:
                adj_list[u][v][0] += bottleneck
            elif u in adj_list[v]:
                adj_list[v][u][0] -= bottleneck

        max_flow += bottleneck

    residual_final = {}
    for i in range(vertex_count):
        residual_final[i] = {}

    for u in adj_list:
        for v in adj_list[u]:
            flow, capacity = adj_list[u][v]
            if capacity - flow > 0:
                residual_final[u][v] = capacity - flow
            if flow > 0:
                residual_final[v][u] = flow

    reachable = set()
    stack = [s]
    while stack:
        u = stack.pop()
        if u not in reachable:
            reachable.add(u)
            for v in residual_final[u]:
                if v not in reachable:
                    stack.append(v)

    min_cut_edges = []
    for u in adj_list:
        if u in reachable:
            for v in adj_list[u]:
                if v not in reachable:
                    min_cut_edges.append((u, v))

    min_cut_edges.sort()

    print(max_flow)
    for u, v in min_cut_edges:
        print(u, v)


if __name__ == "__main__":
    main()
