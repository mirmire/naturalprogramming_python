#!/usr/bin/python3

import random
#  GuessAWord.py  Copyright (c) Kari Laitinen
#  http://www.naturalprogramming.com
#  2009-01-06  First program version created.

#  Solution and conversion to Python version 3 by Prakash Acharya, 17-03-2018
#  Solution also modified to meet PEP8 guidelines for formatting

#  This program is a simple computer game in which the player has to
#  guess the characters of a word, or the player may also try to guess
#  the whole word.
played_words = []


def randomize():
    capitals = ["VIENNA", "HELSINKI", "COPENHAGEN",
                "LONDON", "BERLIN", "AMSTERDAM"]

    word_to_be_guessed = random.choice(capitals)
    return word_to_be_guessed


def ask_user():
    answer = input("\nDo you want to play now?: ")
    if answer.startswith(('Y', 'y')):
        word_to_be_guessed = randomize()
        play(word_to_be_guessed)
    else:
        print('Goodbye! Here is the summary of your game:')
        show_score()
        exit()


def play(word_to_be_guessed):
    guessed_characters = len(word_to_be_guessed) * ["_"]
    number_of_guesses = 0

    def append_to_list(word_to_be_guessed, number_of_guesses):
        played_words.append([word_to_be_guessed, number_of_guesses])
        ask_user()

    # Now guessed_characters refers to a list that contains as
    # many strings "_" as there are characters in the word to be guessed
    while True:
        # input and convert to uppercase
        player_input = input("{} Give a character or word: "
                             .format("".join(guessed_characters))).upper()

        # By writing "".join( guessed_characters ) the list of strings can
        # be converted to a single string.

        if len(player_input) == 1:
            # The player gave a single character
            number_of_guesses += 1
            for character_index in range(len(word_to_be_guessed)):
                if word_to_be_guessed[character_index] == player_input:
                    guessed_characters[character_index] = player_input

            if "_" not in guessed_characters:
                # "_" is not among the guessed characters.
                # This means that all characters have been guessed.
                print("{} Congratulations!!".format(word_to_be_guessed))
                append_to_list(word_to_be_guessed, number_of_guesses)

        elif len(player_input) > 1:
            # The player tried to guess the whole word.
            number_of_guesses += 1
            if player_input == word_to_be_guessed:
                print("\nCongratulations!!! \n")
                append_to_list(word_to_be_guessed, number_of_guesses)
        else:
            # The player gave an empty string.
            # That means that she does not want play any more.
            exit()


def show_score():
    print("\nWORDS          GUESSES")
    for words, counts in played_words:
        print(words.ljust(16), str(counts))


if __name__ == '__main__':
    print("\nThis is a GUESS-A-WORD game  \n")
    ask_user()
