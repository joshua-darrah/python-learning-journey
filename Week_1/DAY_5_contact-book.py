contacts = []  # using a list to store multiple contact dictionaries


def viewContacts():
    if len(contacts) == 0:
        print("\nYour contact list is empty.\n")
    else:
        print("\n=================")
        print("YOUR CONTACT LIST")
        print("=================\n")
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. Name: {contact['name']}")
            print(f"   Number: {contact['number']}")
            print(f"   Email: {contact['email']}\n")


def addContact():
    print("\n================================")
    print("Enter the details you want to add")
    print("================================\n")

    name = input("Enter contact's name: ")
    number = input("Enter contact's number: ")
    email = input("Enter contact's email: ")

    # Creating a contact dictionary and append to list
    contact = {"name": name, "number": number, "email": email}
    contacts.append(contact)

    print(f"\nContact for {name} added successfully!\n")


def removeContact():
    if len(contacts) == 0:
        print("\nYour contact list is empty.\n")
        return

    print("\n========================")
    print("CONTACTS AVAILABLE")
    print("========================\n")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']}")

    try:
        index = int(input("\nEnter the number of the contact to delete: ")) - 1
        if 0 <= index < len(contacts):
            deleted = contacts.pop(index)
            print(f"\nDeleted contact: {deleted['name']}\n")
        else:
            print("\nInvalid selection.\n")
    except ValueError:
        print("\nPlease enter a valid number.\n")


while True:
    print("=============")
    print("CONTACT BOOK")
    print("=============")
    print("1. View all contacts")
    print("2. Add a new contact")
    print("3. Remove a contact")
    print("4. Exit the program\n")

    user_input = input("Select an option: ")

    if user_input == "1":
        viewContacts()
    elif user_input == "2":
        addContact()
    elif user_input == "3":
        removeContact()
    elif user_input == "4":
        print("\nGoodbye!")
        break
    else:
        print("\nInvalid input. Try again.\n")
