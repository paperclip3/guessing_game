import random
import os

def print_game_start():
    print("DIFFICULTIES:")
    print("Easy - 3 Tries - Number Range is 1-10")
    print("Medium - 5 Tries - Number Range is 1-20")
    print("Hard - 10 Tries - Number Range is 1-40")

def clear_console():
    os.system("cls")

def get_difficulty():
    print("Please input the name of the difficulty you choose")
    difficulty = input().lower()
    if difficulty in ["easy", "medium", "hard", "1", "2", "3"]:
        return difficulty
    else:
        print("Invalid difficulty. Please enter a valid difficulty")
        return get_difficulty()

def get_tries_for_diff(diff):
    if diff in ["1", "easy"]:
        return 3
    elif diff in ["2", "medium"]:
        return 5
    elif diff in ["3", "hard"]:
        return 10
    else:
        return None

def get_max_number_for_diff(diff):
    if diff in ["1", "easy"]:
        return 10
    elif diff in ["2", "medium"]:
        return 20
    elif diff in ["3", "hard"]:
        return 40
    else:
        return None

def get_guess():
    guess = int(input())
    return guess

def get_play_again():
    print("Do you want to play again? (Yes/No)")
    player_choice = input().lower()
    return player_choice == "yes"

def game():
    print_game_start()
    diff = get_difficulty()
    tries = get_tries_for_diff(diff)
    max_number = get_max_number_for_diff(diff)
    number = random.randint(1, max_number)
    
    while tries > 0:
        print(f"Guess the number from 1-{max_number}")
        guess = get_guess()
        
        if guess == number:
            print("You guessed the number!")
            if get_play_again():
                print("Ok.")
                game()
            else:
                return
        elif guess < number:
            print("Try again! The correct number is higher.")
        else:
            print("Try again! The correct number is lower.")
        
        tries -= 1

        if tries == 0:
            print(f"You failed to guess the number! It was {number}")
            if get_play_again():
                print("Ok.")
            else:
                return
def main():
    game()

if __name__ == "__main__":
    main()
