#!/usr/bin/python3

import random
#  GuessAWord.py  Copyright (c) Kari Laitinen
#  http://www.naturalprogramming.com
#  2009-01-06  First program version created.
#  2013-10-10  Last modification.
#  Solution and conversion to Python version 3 by Prakash Acharya, 15-03-2018
#  Solution also modified to meet PEP8 guidelines for formatting
#  This program is a simple computer game in which the player has to
#  guess the characters of a word, or the player may also try to guess
#  the whole word.

print("\nThis is a GUESS-A-WORD game  \n")
capitals = ["VIENNA", "HELSINKI", "COPENHAGEN",
            "LONDON", "BERLIN", "AMSTERDAM"]
word_to_be_guessed = random.choice(capitals)

guessed_characters = len(word_to_be_guessed) * ["_"]

# Now guessed_characters refers to a list that contains as
# many strings "_" as there are characters in the word to be guessed

# By writing "".join( guessed_characters ) the list of strings can
# be converted to a single string.

game_is_over = False
while not game_is_over:
    # input and convert to uppercase
    player_input = input("{} Give a character or word: "
                         .format("".join(guessed_characters))).upper()
    if len(player_input) == 1:
        # The player gave a single character
        for character_index in range(len(word_to_be_guessed)):
            if word_to_be_guessed[character_index] == player_input:
                guessed_characters[character_index] = player_input
        if "_" not in guessed_characters:
            # "_" is not among the guessed characters.
            # This means that all characters have been guessed.
            game_is_over = True
            print("".join(guessed_characters) + "  " + "Congratulations!!")
    elif len(player_input) > 1:
        # The player tried to guess the whole word.
        if player_input == word_to_be_guessed:
            print("\nCongratulations!!! \n")
            game_is_over = True
    else:
        # The player gave an empty string.
        # That means that she does not want play any more.
        game_is_over = True
