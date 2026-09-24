import json
import os
from datetime import datetime

FILE_NAME = "expenses.json"


# Load expenses from file
def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


# Save expenses to file
def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


# Add a new expense
def add_expense(expenses):
    title = input("Enter expense name: ")

    try:
        amount = float(input("Enter amount: ₹"))
    except ValueError:
        print("❌ Invalid amount!")
        return

    category = input("Enter category: ")

    expense = {
        "title": title,
        "amount": amount,
        "category": category,
        "date": datetime.now().strftime("%d-%m-%Y")
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("✅ Expense added successfully!")


# View all expenses
def view_expenses(expenses):
    if not expenses:
        print("\nNo expenses found.")
        return

    print("\n========== ALL EXPENSES ==========")

    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i}. {expense['title']} | "
            f"₹{expense['amount']:.2f} | "
            f"{expense['category']} | "
            f"{expense['date']}"
        )


# Calculate total expense
def total_expense(expenses):
    total = sum(expense["amount"] for expense in expenses)

    print(f"\n💰 Total Expense: ₹{total:.2f}")


# Category-wise expense
def category_summary(expenses):
    if not expenses:
        print("\nNo expenses found.")
        return

    categories = {}

    for expense in expenses:
        category = expense["category"]
        categories[category] = categories.get(category, 0) + expense["amount"]

    print("\n======= CATEGORY SUMMARY =======")

    for category, amount in categories.items():
        print(f"{category}: ₹{amount:.2f}")


# Delete expense
def delete_expense(expenses):
    view_expenses(expenses)

    if not expenses:
        return

    try:
        number = int(input("\nEnter expense number to delete: "))

        if 1 <= number <= len(expenses):
            removed = expenses.pop(number - 1)
            save_expenses(expenses)

            print(f"✅ Deleted: {removed['title']}")
        else:
            print("❌ Invalid expense number.")

    except ValueError:
        print("❌ Please enter a valid number.")


# Main program
def main():
    expenses = load_expenses()

    while True:

        print("\n")
        print("================================")
        print("       💰 EXPENSE TRACKER")
        print("================================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Category Summary")
        print("5. Delete Expense")
        print("6. Exit")
        print("================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            total_expense(expenses)

        elif choice == "4":
            category_summary(expenses)

        elif choice == "5":
            delete_expense(expenses)

        elif choice == "6":
            print("\nThank you for using Expense Tracker! 👋")
            break

        else:
            print("❌ Invalid choice. Try again.")


# Start program
if __name__ == "__main__":
    main()
