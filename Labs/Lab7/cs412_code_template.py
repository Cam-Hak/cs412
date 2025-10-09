"""
name: Cameron Hakenson
"""

from collections import deque

# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts


def wfs(graph, start, goal):
    bag = deque()
    marked = set()
    # parent = {}

    bag.append(start)

    while len(bag) != 0:
        v = bag.pop()

        if v in marked:
            continue

        if v == goal:
            print(bag)

        marked.add(v)

        for adj in graph[v]:
            bag.append(adj)


def main():
    graph = {}
    num_segments = int(input())
    for _ in range(num_segments):
        stop = input().split(" ")
        a = stop[0]
        b = stop[1]

        # adds a key for each stop listed and a
        # value for what stops are connected to it

        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)

    start_end = input().split(" ")
    start = start_end[0]
    end = start_end[1]
    wfs(graph, start, end)


if __name__ == "__main__":
    main()
