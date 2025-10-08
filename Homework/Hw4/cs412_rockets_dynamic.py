"""
name: Cameron Hakenson
"""

# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts


def build_rockets(rocket_lengths, target_length):
    num_types = len(rocket_lengths)
    INF = float("inf")

    dp_table = []
    for t in range(num_types + 1):
        row = []
        for length in range(target_length + 1):
            row.append(INF)
        dp_table.append(row)

    for t in range(num_types + 1):
        dp_table[t][0] = 0

    for t in range(1, num_types + 1):
        rocket_size = rocket_lengths[t - 1]
        for length in range(1, target_length + 1):
            if rocket_size > length:
                dp_table[t][length] = dp_table[t - 1][length]
            else:
                skip = dp_table[t - 1][length]
                use_it = dp_table[t][length - rocket_size] + 1
                if skip < use_it:
                    dp_table[t][length] = skip
                else:
                    dp_table[t][length] = use_it

    if dp_table[num_types][target_length] == INF:
        return INF, {}

    rockets_used = {}
    for size in rocket_lengths:
        rockets_used[size] = 0

    length = target_length
    t = num_types

    while length > 0 and t > 0:
        rocket_size = rocket_lengths[t - 1]
        if dp_table[t][length] == dp_table[t - 1][length]:
            t = t - 1
        else:
            rockets_used[rocket_size] = rockets_used[rocket_size] + 1
            length = length - rocket_size

    return dp_table[num_types][target_length], rockets_used


def main():
    rocket_input = input().strip()
    target_length = int(input().strip())

    rocket_lengths = []
    for s in rocket_input.split():
        number = int(s)
        rocket_lengths.append(number)

    min_sections, rockets_used = build_rockets(rocket_lengths, target_length)

    for size in rocket_lengths:
        count = rockets_used[size]
        print(str(count) + " of length " + str(size))

    print(str(min_sections) + " rocket sections minimum")


if __name__ == "__main__":
    main()
