import random

# difficulty selection
def get_difficulty():
    while True: 
        choice = input("Choose difficulty (Easy, Medium, Hard): ").lower()
        if choice == 'easy': 
            return 1, 20, 12 # start & end range, max attempts
        
        elif choice == 'medium':
            return 1, 80, 6

        elif choice == 'hard':
            return 1, 100, 4 

        else: 
            print("Invalid choice. Please enter 'Easy', 'Medium', or 'Hard'.")

# manages rounds
def play_game():
    range_start, range_end, max_attempts = get_difficulty()
    secret_number = random.randint(range_start, range_end)
    attempts = 0
    score = 0

    print(f"\nThinking of a number between {range_start} and {range_end}.")
    print(f"\nYoy have {max_attempts} attempts.")

    while attempts <max_attempts: 
        try: 
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < range_start or guess > range_end:
                print(f"Guess withing range of {range_start} to {range_end}.")

            if guess == secret_number:
                print(f"You did it! You guessed the number in {attempts} attempts.")
                score = calculate_score(max_attempts, attempts)
                print(f"Your score: {score}")
                return score

            elif guess < secret_number:
                print("Too low! Try again.")

            else: 
                print("Too high! Try again.")

        except ValueError: 
            print("Invalid input. Please enter a number.")
    
    print(f"You ran out of attempts! The number was {secret_number}.")
    return 0

# calculate score based on attempts (less attemps  = higher score)
def calculate_score(max_attempts, attempts_taken):
    return max(0, (max_attempts - attempts_taken + 1) * 10)

# loads high score 
def load_high_score():
    try: 
        with open("highscore.txt", "r") as f:
            return int(f.read())
    except (FileNotFoundError, ValueError):
        return 0

# Saves new high score
def save_high_score(score):
    with open("highscore.txt", "w") as f:
        f.write(str(score))

# main function to run game
def main():
    current_high_score = load_high_score()
    print("Welcome to the Guessing Numbers Game!")
    print(f"Curent High Score: {current_high_score}")

    while True: 
        player_score = play_game()
        if player_score > current_high_score: 
                print("New high score!")
                current_high_score = player_score
                save_high_score(current_high_score)

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again != 'yes': 
            break

    print("Thanks for playing!")

if __name__=="__main__":
    main()
        