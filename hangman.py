import random

from words import words

print(words)

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return  word

def hangman():
    word = get_valid_word(words)
    print(word)
    print(type(word))
    word_letter = set(word)
    print(type(word_letter))
    print(word_letter)

    input_letter = input("Enter the letter ")
    used_alphabet = set()
    actual_word = list()
    for x in range(len(word)):
        actual_word.append('_')


    while len(word_letter) != 0:
        used_alphabet.add(input_letter)
        print(f"used letters are {used_alphabet}")
        if  input_letter in word_letter:
            word_letter.remove(input_letter)

            for letter in word :
                if letter == input_letter:
                    actual_word[word.index(letter)] = input_letter
                    print(actual_word)
            #     else:
            #

        else:
            input_letter = input("Enter the letter ")


hangman()