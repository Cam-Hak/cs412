"""Solution for Step 1 of Lab4

Version: 2025
Author: Cameron Hakenson
"""


def isPalindrome(string):
    reversed_string = string[::-1]

    if string == reversed_string:
        return True

    return False


def count_palindromes(word, prev={}):
    if word in prev:
        return prev[word]

    if not word:
        return 1

    valueTemp = 0
    for i in range(1, len(word) + 1):
        # front half of the word is a palindrome
        if isPalindrome(word[:i]):
            # count the number of palindromes in the back half of the word
            valueTemp += count_palindromes(word[i:])
            prev[word] = valueTemp

    return valueTemp


def main():
    number = int(input())
    for _ in range(number):
        word = input()
        print(count_palindromes(word))


if __name__ == "__main__":
    main()
