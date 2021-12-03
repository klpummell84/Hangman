# Imports:
from random import choice
from hangman import stages, words, title, win, lose
#from os import system
from replit import clear
from game import GameManager

# Choose random word from list of words
chosen_word = choice(words)

# create game manager
game = GameManager(chosen_word, 6, True, list(), list())


# Functions: 
def print_display():
    print(f"{' '.join(game.display)}")
def lose_life(guess):
    #system('clear')
    clear()
    game.lives -= 1
    print(f"The word did not contain the letter {guess}, you lose a life!")
    print(stages[game.lives])
    print_display()
    if game.lives <= 0:
        lose_game()
def lose_game():
    #system('clear')
    clear()
    print(lose)
    print("You lose.")
    print(stages[game.lives])
    game.is_playing = False
def win_game():
    #system('clear')
    clear()
    print(win)
    print(f"You Won!, the word was: {game.word.capitalize()}")
    game.is_playing = False
def is_complete():
    '''
    Has the user guessed the whole word?
    '''
    return "_" not in game.display    
def user_turn():
    
    guess = input("Guess a letter: ").lower()
    
    if guess not in game.old_guesses:
        game.old_guesses.append(guess)
    else:
        #system('clear')
        clear()
        print(f"Your guess of letter '{guess.upper()}', was already entered previously")
        print_display()
        return

    correct_guess = False

    for i in range(len(game.word)):
    
        if game.word[i] == guess:
            game.display[i] = guess
            correct_guess = True
            if is_complete():
                win_game()
                return

    if correct_guess:
        #system('clear')
        clear()
        print_display()
    else:
        if game.lives > 0:
            lose_life("\'" + guess.upper() + "\'")
#
#
#
#
#
#
# INTRO(game start)

print(title)

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

# add correct amount of spaces to 'display'
for _ in game.word:
    game.display += "_"

# print initial display
print_display()


####  EXECUTION  ####
while game.is_playing:
    user_turn()