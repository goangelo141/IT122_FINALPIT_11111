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

def main(): #Testing display_word function
    secret_word = "PRUNE" 
    guess_word = "DUNES"
    display_word(secret_word, guess_word)

if __name__ == "__main__":
    main()