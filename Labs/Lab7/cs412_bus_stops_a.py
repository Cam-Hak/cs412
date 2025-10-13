"""
name: Cameron Hakenson
"""

from collections import deque

# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts

def wfs(graph, start, goal):
    # quick sanity check
    if start not in graph or goal not in graph:
        print("no route possible")
        return

    bag = deque()
    marked = set()
    parent = {}

    bag.append(start)
    marked.add(start)
    parent[start] = None

    while bag:
        v = bag.pop()

        if v == goal:
            path = []
            cur = goal
            while cur is not None:
                path.append(cur)
                cur = parent[cur]
            path.reverse()
            print(" ".join(path))
            return

        for adj in graph[v]:
            if adj not in marked:
                marked.add(adj)
                parent[adj] = v
                bag.append(adj)

    print("no route possible")


def main():
    graph = {}
    num_segments = int(input())
    for _ in range(num_segments):
        a, b = input().split(" ")

        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)

    start, end = input().split(" ")
    wfs(graph, start, end)


if __name__ == "__main__":
    main()
