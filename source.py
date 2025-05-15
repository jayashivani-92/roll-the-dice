import random

def roll_dice():
    """Simulate rolling a six-sided dice."""
    return random.randint(1, 6)

def play_game():
    print("Welcome to the Dice Rolling Game!")
    
    while True:
        try:
            rolls = int(input("\nHow many times would you like to roll the dice? "))
            if rolls <= 0:
                print("Please enter a number greater than 0.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        for i in range(rolls):
            result = roll_dice()
            print(f"Roll {i + 1}: You rolled a {result}")
        
        play_again = input("\nWould you like to roll again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    play_game()
