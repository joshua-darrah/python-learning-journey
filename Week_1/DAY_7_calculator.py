print(" Simple Calculator CLI ")
print("Type 'exit' to quit.\n")

while True:
    num1 = input("Enter first number: ")
    if num1.lower() == "exit":
        break
    num2 = input("Enter second number: ")
    operator = input("Enter operator (+, -, *, /): ")

    try:
        num1 = float(num1)
        num2 = float(num2)
        
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2
        else:
            print("Invalid operator!")
            continue

        print(f"Result: {num1} {operator} {num2} = {result}\n")

    except ValueError:
        print("Invalid input. Please enter numbers.\n")
    except ZeroDivisionError:
        print("Error: Division by zero.\n")
