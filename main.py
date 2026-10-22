
# Rion Shionyu

from wordle_functions import choose_word, get_guess
from wordle_functions import evaluate_guess, display_guess, has_won

print("Welcome to Mystery Wordle!")
print("Guess the five-letter word.")
print("G = correct letter and position")
print("Y = correct letter, wrong position")
print("- = letter is not in the word")

sPlayAgain = "yes"

while sPlayAgain == "yes":
    sSecretWord = choose_word()
    lstPreviousGuesses = []
    bWon = False

    # OK for up to six guesses
    for iAttempt in range(1, 7):
        print()
        print("Attempt", iAttempt, "of 6")

        sGuess = get_guess(lstPreviousGuesses)
        lstPreviousGuesses.append(sGuess)

        lstFeedback = evaluate_guess(sGuess, sSecretWord)
        display_guess(sGuess, lstFeedback)

        if has_won(sGuess, sSecretWord):
            print("Congratulations! You solved the puzzle.")
            bWon = True
            break

    # Show the secret word when player loses
    if bWon == False:
        print("Sorry, you ran out of guesses.")
        print("The secret word was:", sSecretWord.upper())

    print()
    sPlayAgain = input("Would you like to play again? (yes/no): ").lower().strip()

print("Thanks for playing!")
