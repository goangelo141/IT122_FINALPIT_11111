import random

def get_secret_word():
    try:
        with open("words.txt", "r") as file:
            word_list = file.read().splitlines() 
        secret_word = random.choice(word_list)
    except FileNotFoundError:
        print("Error: 'words.txt' not found.")
        return None
    except Exception as e:
        print(f"Error occurred: {e}")
        return None
    return secret_word.upper()

def display_word(secret_word, guess_word):
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    GRAY = "\033[90m"
    RESET = "\033[0m"

    print("Your guess result: ")

    for i in range(5):
        if guess_word[i] == secret_word[i]:
            print(f"{GREEN}{guess_word[i]}{RESET}", end=" ")
        elif guess_word[i] in secret_word:
            print(f"{YELLOW}{guess_word[i]}{RESET}", end=" ")
        else:
            print(f"{GRAY}{guess_word[i]}{RESET}", end=" ")
    print("")

def play_game(secret_word):
    attempts = 6
    while attempts > 0:
        guess_word = input("Enter your 5-letter guess: ").upper()

        if len(guess_word) != 5:
            print("Please enter a valid 5-letter word.")
            continue

        display_word(secret_word, guess_word)

        if guess_word == secret_word:
            print("Congratulations! You've guessed the word!")
            return
        else:
            attempts -= 1
            print(f"Attempts remaining: {attempts}")

def main(): 
    secret_word = get_secret_word()
    play_game(secret_word)
    print(f"The secret word was: {secret_word}")

if __name__ == "__main__":
    main()