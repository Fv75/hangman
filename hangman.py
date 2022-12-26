import random
from words import words
import string

def get_word():

    word = random.choice(words)
    guess(word)

def guess(word):
    
    no_guesses = 6
    guessed_letters = set()
    word_letters = set(word)
    print_word = ['_' for i in range(len(word))]

    print(f"I'm thinking of a word. Try to guess it in 7 tries. It has {len(word)} characters")    

    while len(word_letters) > 0:
        print(f"You have {no_guesses + 1} tries left and have used the letters : {' '.join(guessed_letters).upper()}")
        print(*print_word) 

        guess = input("Letter: ").lower()
        guessed_letters.add(guess)

        if guess.isnumeric() or len(guess) <= 0 or len(guess) >= 2:
            print("Please enter a single letter.")

        elif guess in word_letters:
            for i in range(len(word)):
                if word[i] == guess:
                    print_word[i] = guess.upper()
            word_letters.remove(guess)
            print(f"You guessed {guess.upper()}. Correct!") 

        elif no_guesses == 0:
            print("That was your last guess. You lose.")
            print(f"The word was {word.upper()}.")
            break
                               
        else:
            no_guesses -= 1
            print(f"Wrong. Guess again. You have {no_guesses} tries left.")
    if no_guesses > 0:    
        print(*print_word)
        print(f"\nCongratulations! You guessed the word {word.upper()}!\n")

    play_again = input("Do you want to play again? Y/N ")
    if play_again.upper() == 'Y':
            main()
            

def main():
    get_word()

if __name__ == '__main__':
    main()



