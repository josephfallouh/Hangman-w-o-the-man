# Python Program Hangman Game - Joseph Fallouh
import random, sys

# pool of words from which will be randomly selected
wordSelection = '''running fanta scooter pitch field automobile telephone
water astronaut mountain philanthropy metropolitan baseball trophy swimming
python programming scripting scrabble cybersecurity multiply company'''

wordSelection = wordSelection.split(' ')

# this function randomly selects a word from the pool above
def select_word(wordSelection_):
    return random.choice(wordSelection_)

# this function returns remaing chances
def get_remaining_chanes(chances_):
    return chances_

# this function displays each character as an underscore, to let the player know how many characters the word is
def print_blank_word_initial(word_):
    return ("_  " * len(word_))

# this function will update the lines with the guesssed letters
def print_blank_word(word_, guessedLetter_):
    displayWord = ""
    for i in word_:
        if i in guessedLetter_:
            displayWord += i + " "
        else:
            displayWord += "_ "

    return displayWord


if __name__ == '__main__':
    word = select_word(wordSelection)

    # this if-else is determining how many chances the player gets, if the word is greater than 6 characters,
    # they will get the length of the word, plus three chances. 
    if len(word) > 6:
        chances = len(word) + 3
    else:
        chances = len(word) + 2

    print()
    print("Welcome to Hangman! Lets Begin.")
    print()
    print()
    print(print_blank_word_initial(word))
    print()

    guessedLetters = []
    for i in range(chances):
        print("You have " + str(get_remaining_chanes(chances)) + " chances left!")
        
        # gets the guessed letter from the user
        guessedLetter = input("Guess a Letter:  ")
        print()

        # if the user guessed correctly, the letter will be added to the list declared above as 'guessedLetters'
        if guessedLetter in word:
            guessedLetters.append(guessedLetter)

        # this will update the lines to add the correctly guessed letters
        displayedWord = print_blank_word(word, guessedLetters)
        print(displayedWord)

        # since an attempt was used, we will decrease chances by 1
        print()
        chances = chances - 1

        # if all the letters in the list 'guessedLetters' match the letters in 'word', you win if not, you lose. 
        if all(letter in guessedLetters for letter in word):
            print("Congratulations! You guessed the word!")
            print()
            sys.exit()

print("Sorry, you lost. The word was", word)
print()