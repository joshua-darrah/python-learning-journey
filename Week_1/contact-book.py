contacts = {}



def viewContact():
    if len(contacts) == 0:
        print('')
        print("Your contact list is empy")
        print('')
        
    else:
        print(f'=================')
        print("YOUR CONTACT LIST")
        print(f'=================')
        print('')
        print(f'Name: {contacts['name']}')
        print(f'Number: {contacts["number"]}')
        print(f'Email: {contacts['email']}')
        print('')


def addContact():
    print(f'================================') 
    print('Enter the details you want to add')
    print(f'================================') 
    print("Enter Contact's name")
    contacts["name"] = input('>>>   ')
    print('')
    print("Enter Contact's number")
    contacts["number"] = input('>>>   ')
    print('')
    print("Enter Contact's email")
    contacts["email"] = input('>>>   ')
    print('')
    print(contacts)


def removeContact():
    print(list(contacts))
    print(f'====================================')
    print('Select the contact you want to delete')
    print(f'====================================') 
    contactSubstraction = int(input('>>>   '))
    contacts.pop(contactSubstraction)
    print('')



while True:
    print(f'============')
    print(f'CONTACT BOOK')
    print(f'============')
    print(f'1. View all contacts')
    print(f'2. Add a new contact')
    print(f'3. Remove a contact')
    print(f'4. Exit the program')
    print('')

    user_input = input("Select an option:  ")
    if user_input == "1":
        viewContact()

    elif user_input == "2":
        addContact()
    
    elif user_input == "3":
        removeContact()

    elif user_input == "4":
        exit()

    else:
        print("Invalid input")


