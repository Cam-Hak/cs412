"""Solution for Step 2 of Lab4

Version: 2025
Author: Cameron Hakenson
"""


def isPalindrome(string):
    reversed_string = string[::-1]

    if string == reversed_string:
        return True

    return False


def count_palindromes(word):
    prev = [-1] * (len(word) + 1)

    def helper(i):
        if i == len(word):
            return 1
        if prev[i] != -1:
            return prev[i]

        count = 0
        for j in range(i + 1, len(word) + 1):
            if isPalindrome(word[i:j]):
                count += helper(j)

        prev[i] = count
        return count

    return helper(0)


def main():
    number = int(input())
    for _ in range(number):
        word = input()
        print(count_palindromes(word))


if __name__ == "__main__":
    main()
