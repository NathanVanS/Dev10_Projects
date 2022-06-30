from pickle import APPEND # i have no idea where this came from or the line below
from venv import create
import random

word_list = []
used_words = []
revealed_word_List = []
guessed_Letters = []
incorrect_Letters = []
guessed_letter = " "
losses = 0
wins = 0

with open("words_alpha.txt", "r") as file:
    all_words = file.read()
    answers = list(map(str, all_words.split()))

def pick_word(): #Generates the word, adds to used words list, checks if it has been used already
    word = random.choice(answers)
    print(word)
    if word in used_words:
        pick_word()
    else:
        used_words.append(word)
    return list(word)

def create_blank_list(word): # creates the initial blank revealed word

    for i in word:
        revealed_word_List.append("_")

def print_the_stuff(): # does the three prints
    
    print(revealed_word_List)
    print(guessed_Letters)
    print(incorrect_Letters)

def get_input(): # gets the input try catches for string, checks for repeat, and returns value
    try:
        guessed_letter = input("Enter a letter.")
        if guessed_letter in guessed_Letters:
            print("You already guessed that.")
            get_input()
        if type(guessed_letter) is not str:
            ValueError
    except ValueError:
        print("Hey, it's a letter.")
        get_input()
    return guessed_letter

def find_letter_index(guessed_letter): # takes the input, checks for a match, and puts it in the correct list
    correct_guess = True
    index = -1

    for i in word_list:
        index += 1
        if i == guessed_letter:
            revealed_word_List[index] = guessed_letter
            guessed_Letters.append(i)
            correct_guess = False
    if correct_guess:
        incorrect_Letters.append(guessed_letter)

def play(): # this is the play loop, registers wins losses, and asks to play again

    global wins
    global losses
    play_again = input("Play? yes or no")
    
    if "y" in play_again:

        word_list = pick_word()
        create_blank_list(word_list)

        while "_" in revealed_word_List:
            if len(incorrect_Letters) < 8:      
                find_letter_index(get_input())
            else:
                print("You lose.") 
                losses += 1
                break
            wins += 1
        print_the_stuff()
        play()
    elif "n" in play_again:
        print("Thanks for playing")

play()