# iterative dfs
def it_dfs(graph, start):
    stack = [start]
    visited = [start]

    while stack:
        current = stack.pop()
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.append(neighbor)
                stack.append(neighbor)

    return visited


# recursive dfs
def rec_dfs(graph, v, visited=None):
    if visited is None:
        visited = set()

    visited.add(v)
    for n in graph[v]:
        if n not in visited:
            rec_dfs(graph, n, visited)
    return visited


graph = {"A": ["B", "C"], "B": ["D"], "C": ["E"], "D": [], "E": []}

print(it_dfs(graph, "A"))
print(rec_dfs(graph, "A"))
