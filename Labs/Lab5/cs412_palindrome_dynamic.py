"""
name: Cameron Hakenson
"""

# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts


def isPalindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string


def count_palindromes(word):

    # make dp table
    dp_table = [0] * (len(word) + 1)
    dp_table[len(word)] = 1

    # fill table backwards?
    for i in range(len(word) - 1, -1, -1):
        count = 0
        for j in range(i + 1, len(word) + 1):
            # checking if substring is palindrome
            if isPalindrome(word[i:j]):
                count += dp_table[j]
        dp_table[i] = count

    return dp_table[0]


def main():
    number = int(input())
    for _ in range(number):
        word = input()
        print(count_palindromes(word))


if __name__ == "__main__":
    main()
