"""
Welcome to the John`s HANGMAN game!!!
There's no time to explain! Rather, start the game, because it is interesting and exciting!
Joke
My game has a very simple interface. Using the selector, which you will get into at the beginning and after each game,
you can either start the next execution, or look at the words that you came across earlier.
During the game, you should enter one letter at a time (the case is not important), then press Enter. You have the
opportunity to make a mistake 7 times. After that, you will see a message and will soon be taken to the menu.
In case of guessing the word, you will see the corresponding message and will also soon get to the menu for a new round.
"""
from random import randint  # for random-selected word
from os import system       # for clear console
from time import sleep      # for wait after end of game


def word_for_game() -> str:
    """
    This function :returns one word from words_collection.txt file
    """
    words_collection = open('words_collection.txt', 'r')
    string_of_words = words_collection.readline()
    unpacked_string_of_words = string_of_words.split(' ')
    words_collection.close()
    return unpacked_string_of_words[randint(0, len(unpacked_string_of_words)-1)]


def game_logic():
    """
    This function contains the logic of the game itself.
    She accepts the word that prepares for the game.
    Also, it processes the entered letters for the presence in the hidden word.
    """
    current_word = word_for_game()
    words_history_list.append(current_word)
    solution_field = ['_' for i in range(len(current_word))]
    misses_letters = []
    current_word_list = list(current_word)
    while len(misses_letters) <= 7 or solution_field in current_word_list:
        letter: str = (visual_interface_printer(solution_field, misses_letters))
        if letter in current_word_list:
            for letter_index in range(len(current_word_list)):
                if letter == current_word_list[letter_index]:
                    solution_field[letter_index] = current_word_list[letter_index]
        else:
            misses_letters.append(letter)
            if letter == 'drop_this_user_into_menu':
                system('clear')
                return


def visual_interface_printer(solution_field, misses_letters) -> str:
    """
    Functions with output are not the best idea, and I know it. But since we work in the console and, moreover, with
    pseudo-graphics, I think I did the right thing.
    This is a printer function. Depending on the current state of the game, after erasing the old state, it varies the
    picture on the screen. It also accepts a new letter from the user and reports the result of the end of the game.
    :param solution_field: shows hidden and guessed letters
    :param misses_letters:stores miss letters and (implicitly) their number
    :return: every new letter, inputted by user
    """
    system('clear')
    print(f'   ┃┣━━━━━━┳━\tWord: {solution_field}\n'                 # line1
          f'   ┃┃      ┃ \tMissed letters: {misses_letters}')        # line2
    print('   ┃┃     ()') if len(misses_letters) > 0 else print('   ┃┃')  # line3

    if len(misses_letters) > 3:                                           # line4
        print('   ┃┃     ╱▊\\')
    elif len(misses_letters) == 3:
        print('   ┃┃     ╱▊')
    elif len(misses_letters) == 2:
        print('   ┃┃      ▊')
    else:
        print('   ┃┃')
    print('   ┃┃      ▊') if len(misses_letters) > 4 else print('   ┃┃')  # line5

    if len(misses_letters) == 6:                                           # line4
        print('   ┃┃     ╱')
    elif len(misses_letters) == 7:
        print('   ┃┃     ╱ \\')
    else:
        print('   ┃┃')
    print('   ┃┃')
    if len(misses_letters) >= 7:
        print('___▉▉____________\tYou lost (X_X):\n\nwait a bit')
        sleep(4)
        return 'drop_this_user_into_menu'
    if '_' not in solution_field:
        print('___▉▉____________\tCongratulations!!! You WON! (^_^)\n\nwait a bit')
        sleep(4)
        return 'drop_this_user_into_menu'
    return input('___▉▉____________\t your new letter: ').lower()


print('\t\tHello!\nYou came into my hangman game. \nChoose and write the option below:')
words_history_list = []
while True:
    i_want_do = int(input(' 1   -- I want start the hangman\n'
                          ' 2   -- I want look for previous words\n'
                          'else -- Exit\n:'))
    if i_want_do == 1:
        game_logic()
    elif i_want_do == 2:
        print(words_history_list)
    else:
        exit(0)