import csv

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g. Food, Transport): ")
    amount = input("Enter amount (GHS): ")

    with open("expenses.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, category, amount])
    print("Expense added successfully!")

def view_expenses():
    print("\n--- Your Expenses ---")
    with open("expenses.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

def main():
    while True:
        print("\n=== Simple Expense Tracker ===\n")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

main()
