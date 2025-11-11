"""
name: Cameron Hakenson
"""

import math


def main():
    m = int(input())

    currencies = set()
    edges = []

    for _ in range(m):
        parts = input().split()
        c_in = parts[0]
        c_out = parts[1]
        rate = float(parts[2])

        currencies.add(c_in)
        currencies.add(c_out)
        edges.append((c_in, c_out, -math.log(rate), rate))

    currencies = list(currencies)
    n = len(currencies)

    dist = {c: 0 for c in currencies}
    pred = {c: None for c in currencies}

    for _ in range(n - 1):
        for c_in, c_out, weight, rate in edges:
            if dist[c_in] + weight < dist[c_out]:
                dist[c_out] = dist[c_in] + weight
                pred[c_out] = c_in

    cycle_node = None
    for c_in, c_out, weight, rate in edges:
        if dist[c_in] + weight < dist[c_out]:
            cycle_node = c_out
            break

    if cycle_node is None:
        print("No Arbitrage Detected")
    else:
        print("Arbitrage Detected")

        current = cycle_node
        for _ in range(n):
            current = pred[current]

        cycle = [current]
        next_node = pred[current]
        while next_node != current:
            cycle.append(next_node)
            next_node = pred[next_node]

        cycle.reverse()

        rate_map = {}
        for c_in, c_out, weight, rate in edges:
            rate_map[(c_in, c_out)] = rate

        factor = 1.0
        for i in range(len(cycle)):
            factor *= rate_map[(cycle[i], cycle[(i + 1) % len(cycle)])]

        print(" => ".join(cycle + [cycle[0]]))
        print(f"{factor:.5f} factor increase")


if __name__ == "__main__":
    main()
