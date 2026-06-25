expenses = []

def add_expense():
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")

        expense = {
            "amount": amount,
            "category": category
        }

        expenses.append(expense)

        print("Expense added successfully!")

    except ValueError:
        print("Please enter a valid amount.")


def view_expenses():
    if len(expenses) == 0:
        print("No expenses recorded.")
        return

    print("\n--- Expenses ---")

    for expense in expenses:
        print(
            f"Category: {expense['category']} | Amount: ₹{expense['amount']}"
        )


def total_expenses():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"\nTotal Spending: ₹{total}")


while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spending")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expenses()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")