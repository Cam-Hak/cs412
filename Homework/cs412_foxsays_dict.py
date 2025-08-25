"""Homework 1

Author: Cameron Hakenson

Honor Code and Acknowledgments:
    This work complies with the JMU Honor Code.

Solution only using sets
"""

def main():
    sound_input = input()
    num_sounds = int(input())
    animals_sounds = {}
    animals_heard = []
    fox_sounds = []

    split_sound_input = sound_input.split(" ")
    for i in range(num_sounds):
        animal_sound = input()
        split_animal_sound = animal_sound.split("goes ")
        animals_sounds[split_animal_sound[1]] = split_animal_sound[0].strip()

    for i in range(len(split_sound_input)):
        animal_sound = animals_sounds.get(split_sound_input[i])
        if animal_sound:
            if animals_heard.count(animal_sound) == 0:
                animals_heard.append(animal_sound)
        else:
            fox_sounds.append(split_sound_input[i])

    input()

    print("what the fox says: ", end="")
    print(' '.join(fox_sounds))
    print("also heard: ", end="")
    print(' '.join(animals_heard))

if __name__ == "__main__":
    main()
