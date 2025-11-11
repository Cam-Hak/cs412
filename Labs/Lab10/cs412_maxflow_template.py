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


if __name__ == "__main__":
    main()
