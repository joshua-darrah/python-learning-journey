tasks = []

def viewTask():
    if len(tasks) == 0:
        print('')
        print("Your list is empy")
        print('')
        
    else:
        print(f'===========')
        print("YOUR TASKS")
        print(f'===========')
        for task in tasks:
            print('')
            print(task)
            print('')


def addTask():
    print(f'=========================================') 
    print('Enter the task you want to add to the list')
    print(f'=========================================') 
    taskAddition = input('>>>   ')
    tasks.append(taskAddition)
    print('')


def removeTask():
    print(list(tasks))
    print(f'==================================')
    print('Select the task you want to delete')
    print(f'==================================') 
    taskSubstraction = int(input('>>>   '))
    tasks.remove(tasks[taskSubstraction - 1])
    print('')



while True:
    print(f'==================')
    print(f'TO DO LIST MANAGER')
    print(f'==================')
    print(f'1. View all tasks')
    print(f'2. Add a new task')
    print(f'3. Remove a task')
    print(f'4. Exit the program')
    print('')

    user_input = input("Select an option:  ")
    if user_input == "1":
        viewTask()

    elif user_input == "2":
        addTask()
    
    elif user_input == "3":
        removeTask()

    elif user_input == "4":
        exit()

    else:
        print("Invalid input")

