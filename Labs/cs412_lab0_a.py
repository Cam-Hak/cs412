"""Lab 0

Author: Cameron Hakenson

Honor Code and Acknowledgments:
    This work complies with the JMU Honor Code.

1. I used the Dictionary/Map data structure

2. I used the .get() operation on the dictionary

3. The runtime should be in O(1) for the get operation

4. My algorithm runs in O(n)

5. My algorithm works because after each word and its translation
   is loaded into the dictionary, I split the given sentence and replace
   each word in the sentence with its translation and join the split
   sentence with a space.
"""

def main():
    word_dict = {}

    # getting the number of words and loading them into dictionary
    num_words = int(input())
    for i in range(num_words):
        word = input()
        split_word = word.split(" ")
        word_dict[split_word[1]] = split_word[0]

    # getting sentence and translating based on words gathered in dictionary
    sentence = input()
    split_sentence = sentence.split(" ")
    for i, word in enumerate(split_sentence):
        translated_word = word_dict.get(word)
        if translated_word:
            split_sentence[i] = translated_word
        else:
            split_sentence[i] = "???"

    translated_sentence = " ".join(split_sentence)
    print(f"{translated_sentence} ")

if __name__ == "__main__":
    main()
