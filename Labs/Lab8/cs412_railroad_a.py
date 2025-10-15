"""
name: Cameron Hakenson
"""

# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts


from connected_components import count_and_label
import math


# calculates distance between two points
def calc_distance(points1, points2):
    return round(math.dist(points1, points2), 1)


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
    forest = {}
    count, labels = count_and_label(graph)
    while count > 1:
        pass


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


if __name__ == "__main__":
    main()
