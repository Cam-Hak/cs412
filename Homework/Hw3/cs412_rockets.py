"""
name: Cameron Hakenson
"""

# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts


def minimum_rocket_sections(rocket_list, desired_length):
    min_sections = float("inf")
    best_sequence = {}
    rocket_seq = {}
    for r in rocket_list:
        rocket_seq[str(r)] = 0

    def rocket_search(len_remaining, depth, sequence):
        nonlocal min_sections, best_sequence

        if len_remaining < 0:
            return

        if len_remaining == 0 and depth < min_sections:
            min_sections = depth
            best_sequence = sequence.copy()
            return

        for r in rocket_list:
            sequence[str(r)] += 1
            rocket_search(len_remaining - r, depth + 1, sequence)
            sequence[str(r)] -= 1

    rocket_search(desired_length, 0, rocket_seq)

    for rocket in best_sequence.keys():
        print(f"{best_sequence[rocket]} of length {rocket}")
    return min_sections


def main():
    rocket_list = []
    available_rockets = input()
    desired_length = int(input())
    rockets_split = available_rockets.split(" ")

    for rocket in rockets_split:
        rocket_list.append(int(rocket))

    min_sections = minimum_rocket_sections(rocket_list, desired_length)
    print(f"{min_sections} rocket sections minimum")


if __name__ == "__main__":
    main()
