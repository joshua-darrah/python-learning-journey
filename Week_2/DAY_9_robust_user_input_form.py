def get_user_info():
    try:
        name = input("Enter your name: ")
        if name == '':
            raise ValueError("Name cannot be empty!")

        age = int(input("Enter your age: "))
        if age <= 0:
            raise ValueError("Age must be greater than 0!")

    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("Unexpected error:", e)
    else:
        print(f"\nWelcome {name}! You are {age} years old.")
    finally:
        print("Form submission completed.\n")

# Run the function
get_user_info()
