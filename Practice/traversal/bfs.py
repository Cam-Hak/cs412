from collections import deque


def it_bfs(graph, start):
    visited = set([start])
    parent = {start: None}
    order = []

    q = deque([start])
    while q:
        v = q.popleft()
        order.append(v)
        for w in graph[v]:
            if w not in visited:
                visited.add(w)
                parent[w] = v
                q.append(w)

    return order, parent


# graph = {"A": ["B", "C"], "B": ["D"], "C": ["E"], "D": [], "E": []}
graph = {"A": ["B", "D"], "B": ["A", "E"], "D": ["A", "E"], "E": ["B", "D"]}

order, parent = it_bfs(graph, "A")

for node in order:
    print(f"node: {node} -> parent: {parent[node]}")
