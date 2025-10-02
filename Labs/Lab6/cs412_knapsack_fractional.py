"""
name: Cameron Hakenson
"""

# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts


def fractional_knapsack(capacity, items):
    items = [(name, value, weight, value / weight) for (name, value, weight) in items]

    def ratio_key(item):
        return item[3]

    items.sort(key=ratio_key, reverse=True)

    total_value = 0.0
    knapsack_contents = []

    for name, value, weight, ratio in items:
        if capacity <= 0:
            break

        if weight <= capacity:
            knapsack_contents.append(f"{name}({value:.2f}, {weight:.2f})")
            total_value += value
            capacity -= weight
        else:
            fraction_value = ratio * capacity
            knapsack_contents.append(f"{name}({fraction_value:.2f}, {capacity:.2f})")
            total_value += fraction_value
            capacity = 0

    print(" ".join(knapsack_contents))
    print(total_value)


def main():
    import sys

    data = sys.stdin.read().strip().splitlines()
    W = int(data[0])
    n = int(data[1])

    items = []
    for i in range(n):
        name, value, weight = data[2 + i].split()
        items.append((name, float(value), float(weight)))

    fractional_knapsack(W, items)


if __name__ == "__main__":
    main()
