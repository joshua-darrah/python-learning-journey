import random


print(f"Guess a number from 1 to 10")
attempts = 0

while attempts < 3:
    num = random.randint(1, 10)
    guess = int(input("Enter your guess here:   "))
    attempts += 1
    if guess == num:
       print(f"Congratulations! You guessed right.")
       print(f"The number is indeed {guess}. You guessed it right in {attempts} attempts.")
       break
    elif guess > num:
        print("Oops, your guess is larger than the number.")
        print("Try again!")
      
    else:
        print("Oops, that was close but your guess is smaller than the number")
        print("Try again!")
 