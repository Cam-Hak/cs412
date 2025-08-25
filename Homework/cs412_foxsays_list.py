"""Homework 1

Author: Cameron Hakenson

Honor Code and Acknowledgments:
    This work complies with the JMU Honor Code.

Solution only using lists
"""

def main():
    sound_input = input()
    num_sounds = int(input())
    animals_sounds = []
    animals_heard = []
    fox_sounds = []

    split_sound_input = sound_input.split(" ")
    for i in range(num_sounds):
        animal_sound = input()
        split_animal_sound = animal_sound.split("goes ")
        animals_sounds.append([split_animal_sound[0].strip(), split_animal_sound[1]])

    for i in range(len(split_sound_input)):
        found = False
        for j in range(len(animals_sounds)):
            if split_sound_input[i] == animals_sounds[j][1]:
                found = True
                if animals_heard.count(animals_sounds[j][0]) == 0:
                    animals_heard.append(animals_sounds[j][0])

        if not found:
            fox_sounds.append(split_sound_input[i])

    input()

    print("what the fox says: ", end="")
    print(' '.join(fox_sounds))
    print("also heard: ", end="")
    print(' '.join(animals_heard))

if __name__ == "__main__":
    main()
