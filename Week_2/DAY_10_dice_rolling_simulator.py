import random  

def roll_dice():
    print("Dice Rolling Simulator")
    while True:
        input("Press Enter to roll the dice... ")
        dice = random.randint(1, 6)  # random number between 1 and 6
        print(f"You rolled a {dice}!\n")

        choice = input("Do you want to roll again? (y/n): ").lower()
        if choice != 'y':
            print("Thanks for playing!")
            break

# Running the dice roller
roll_dice()
