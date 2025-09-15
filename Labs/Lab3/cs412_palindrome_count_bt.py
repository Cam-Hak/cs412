"""
name: Cameron Hakenson
"""

# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts


# helper function determining if a string is a palindrome
def is_palindrome(p_string):
    return p_string == p_string[::-1]


# gets all the partitions based on string and index
def get_partitions(p_string, curr_index):
    num_partitions = 0

    if curr_index == len(p_string):
        return 1

    for i in range(curr_index, len(p_string)):
        if is_palindrome(p_string[curr_index: i + 1]):
            num_partitions += get_partitions(p_string, i + 1)

    return num_partitions


def main():
    p_string_list = []
    num_palindromes = int(input())
    for _ in range(num_palindromes):
        palindrome = input()
        p_string_list.append(palindrome)

    for p_string in p_string_list:
        print(get_partitions(p_string, 0))


if __name__ == "__main__":
    main()
