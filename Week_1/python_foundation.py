### DAY ONE

##greeting
# name = input('Enter your name: ')
# hubby = input('Enter your hubby:  ')

# print(f'Hello, {name}!')
# print(f'{hubby} sounds fun!')


##simple calcultor
# x = 10
# y = 3

# print("Addition:", x + y)
# print("Subtraction:", x - y)
# print("Multiplication:", x * y)
# print("Division:", x / y)
# print("Floor Division:", x // y)  # rounds down
# print("Modulus:", x % y)          # remainder

# __________________________________________________________________________________________________


###      DAY TWO

## Grade Classifier

# score = int(input("Enter your score (0-100): "))

# if score >= 90:
#     grade = "A"
# elif score >= 80:
#     grade = "B"
# elif score >= 70:
#     grade = "C"
# elif score >= 60:
#     grade = "D"
# elif score >= 50:
#     grade = "E"
# else:
#     grade = "F"

# print(f"Your grade is: {grade}")


##Login Check System

# username = input("Enter username: ")
# password = input("Enter password: ")

# # correct credentials
# correct_username = "admin"
# correct_password = "12345"

# if username == correct_username and password == correct_password:
#     print("Login successful!")
# else:
#     print("Invalid username or password")

# __________________________________________________________________________________________________


### DAY THREE

## Sum of numbers from 1 to 100

# total = 0

# for i in range(1, 101):
#     total += i

# print("The sum of numbers from 1 to 100 is:", total)


# import random

# print(f"Guess a number from 1 to 10")
# attempts = 0


# while attempts < 3:
#     num = random.randint(1, 10)
#     guess = int(input("Enter your guess here:   "))
#     attempts += 1

#     if guess == num:
#         print(f"Congratulations! You guessed right.")
#         print(f"The number is indeed {guess}. You guessed it right in {attempts} attempts.")
#         break

#     elif guess > num:
#         print("Oops, your guess is larger than the number.")
#         print("Try again!")
       

#     else:
#         print("Oops, that was close but your guess is smaller than the number")
#         print("Try again!")

# __________________________________________________________________________________________________




### DAY FOUR

# tasks = []

# def viewTask():
#     if len(tasks) == 0:
#         print('')
#         print("Your list is empy")
#         print('')
        
#     else:
#         print(f'===========')
#         print("YOUR TASKS")
#         print(f'===========')
#         for task in tasks:
#             print('')
#             print(task)
#             print('')


# def addTask():
#     print(f'=========================================') 
#     print('Enter the task you want to add to the list')
#     print(f'=========================================') 
#     taskAddition = input('>>>   ')
#     tasks.append(taskAddition)
#     print('')


# def removeTask():
#     print(list(tasks))
#     print(f'==================================')
#     print('Select the task you want to delete')
#     print(f'==================================') 
#     taskSubstraction = int(input('>>>   '))
#     tasks.remove(tasks[taskSubstraction - 1])
#     print('')



# while True:
#     print(f'==================')
#     print(f'TO DO LIST MANAGER')
#     print(f'==================')
#     print(f'1. View all tasks')
#     print(f'2. Add a new task')
#     print(f'3. Remove a task')
#     print(f'4. Exit the program')
#     print('')

#     user_input = input("Select an option:  ")
#     if user_input == "1":
#         viewTask()

#     elif user_input == "2":
#         addTask()
    
#     elif user_input == "3":
#         removeTask()

#     elif user_input == "4":
#         exit()

#     else:
#         print("Invalid input")

# import re as r

# word = input(" ")
# search = r.search(r"JOC", word)

# print(bool(search))