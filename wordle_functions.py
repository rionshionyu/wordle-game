
# Rion Shionyu
# Level #7 Assignment Wordle
import random


# Choose a random five-letter word
def choose_word():
    lstWords = ["plant", "crane", "slate", "brick", "ghost",
                "flame", "chair", "bread", "mouse", "train"]
    return random.choice(lstWords)


# Get a guess of a player
def get_guess(lstPreviousGuesses):
    while True:
        sGuess = input("Enter a five-letter word: ").lower().strip()

        if len(sGuess) != 5 or not sGuess.isalpha():
            print("Please enter exactly five letters.")
        elif sGuess in lstPreviousGuesses:
            print("You already guessed that word. Try again.")
        else:
            return sGuess


# Check each letters in the guess
def evaluate_guess(sGuess, sSecretWord):
    lstFeedback = []

    for iCount in range(5):
        if sGuess[iCount] == sSecretWord[iCount]:
            lstFeedback.append("G")
        elif sGuess[iCount] in sSecretWord:
            lstFeedback.append("Y")
        else:
            lstFeedback.append("-")

    return lstFeedback


# Show the guess and feedback
def display_guess(sGuess, lstFeedback):
    print("Guess:", " ".join(sGuess.upper()))
    print("Feedback:", " ".join(lstFeedback))


# Check if the player guessed the word right
def has_won(sGuess, sSecretWord):
    return sGuess == sSecretWord
