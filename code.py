import random

def roll_dice():
    return random.randint(1, 6)

def main():
    print("Welcome to the Dice Simulator!")
    num_players = int(input("Enter the number of players: "))
    
    while True:
        input("Press Enter to roll the dice...")
        dice_result = roll_dice()
        print(f"The dice rolled: {dice_result}")
        
        play_again = input("Roll again? (y/n): ")
        if play_again.lower() != 'y':
            break

    print("Thank you for playing the Dice Simulator!")

if __name__ == "__main__":
    main()
