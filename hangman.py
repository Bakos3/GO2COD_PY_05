import random
import requests

def fetch_random_word(length=6):
    try:
        response = requests.get(f"https://random-word-api.herokuapp.com/word?number=1&length={length}")
        if response.status_code == 200:
            return response.json()[0] 
        else:
            print("Error fetching word, using default word instead.")
            return "hangman"
    except Exception as e:
        print(f"An error occurred: {e}, using default word instead.")
        return "hangman"

def hangman():
    difficulty = 6  
    while True:
        word = fetch_random_word(difficulty)
        guessed_word = ["_" for _ in word] 
        attempts = 6
        guessed_letters = set()

        print("\nWelcome to Hangman!")
        print(f"Word Length: {len(word)}")

        while attempts > 0:
            print("\nWord: " + " ".join(guessed_word))
            print(f"Attempts left: {attempts}")
            print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")

            guess = input("Guess a letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Please guess a single letter.")
                continue

            if guess in guessed_letters:
                print("You already guessed that letter.")
                continue

            guessed_letters.add(guess)

            if guess in word:
                print("Good guess!")
                for i, letter in enumerate(word):
                    if letter == guess:
                        guessed_word[i] = guess
                
                if "_" not in guessed_word:
                    print("\nCongratulations! You guessed the word: " + word)
                    break
            else:
                print("Wrong guess!")
                attempts -= 1

        else:
            print("\nGame over! The word was: " + word)

        choice = input("\nDo you want to play again? (yes/no): ").lower().strip()
        if choice == "yes":
            difficulty += 2
            print("\nIncreasing difficulty! Words will be longer now.")
        else:
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    hangman()
