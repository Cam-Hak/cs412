"""
name: Cameron Hakenson
"""

# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts


from connected_components import count_and_label
import math


# calculates distance between two points
def calc_distance(points1, points2):
    return math.dist(points1, points2)


# creates the graph using adj format
def make_adj(points):
    adj_list = {}
    for i in range(len(points)):
        adj_list[i] = {}
        for key, value in points.items():
            if i == key:
                continue

            adj_list[i][key] = calc_distance(points[i], value)

    return adj_list


def boruvka(graph):
    forest = {i: {} for i in graph}
    count, labels = count_and_label(forest)
    seen_edges = set()
    total = 0

    # gathers all the edges
    edges = []
    for u in graph:
        for v, w in graph[u].items():
            if u < v:
                edges.append((u, v, w))

    while count > 1:
        safe = {}

        for u, v, w in edges:
            if labels[u] != labels[v]:
                if labels[u] not in safe or w < safe[labels[u]][2]:
                    safe[labels[u]] = (u, v, w)
                if labels[v] not in safe or w < safe[labels[v]][2]:
                    safe[labels[v]] = (u, v, w)

        for u, v, w in safe.values():
            edge = (min(u, v), max(u, v))
            if edge in seen_edges:
                continue
            forest[u][v] = w
            forest[v][u] = w
            seen_edges.add(edge)
            total += w

        count, labels = count_and_label(forest)

    return total


def calc_cost(mst):
    for value in mst.values():
        for v in value:
            print(v)


def main():
    points = {}
    num_cities = int(input())
    count = 0
    for _ in range(num_cities):
        city_points = input().split()
        city_points = list(map(float, city_points))
        points[count] = city_points
        count += 1

    graph = make_adj(points)
    cost = boruvka(graph)
    print(f"${cost:.1f}M")


if __name__ == "__main__":
    main()
