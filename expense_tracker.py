import json
import os
from datetime import datetime

DATA_FILE = 'expenses.json'


# Load expenses from JSON file
def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)


# Save expenses to JSON file
def save_expenses(expenses):
    with open(DATA_FILE, 'w') as f:
        json.dump(expenses, f)


# Add an expense
def add_expense(description, amount):
    expenses = load_expenses()
    if amount < 0:
        print("Error: Amount cannot be negative.")
        return
    expense = {
        'id': len(expenses) + 1,
        'date': datetime.now().strftime('%Y-%m-%d'),
        'description': description,
        'amount': amount
    }
    expenses.append(expense)
    save_expenses(expenses)
    print(f"Expense added successfully (ID: {expense['id']})")


# List all expenses
def list_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses found.")
        return
    print(f"{'ID':<5} {'Date':<11} {'Description':<12} {'Amount':<7}")
    for exp in expenses:
        print(f"{exp['id']:<5} {exp['date']:<11} {exp['description']:<12} ${exp['amount']}")


# Delete an expense
def delete_expense(expense_id):
    expenses = load_expenses()
    for exp in expenses:
        if exp['id'] == expense_id:
            expenses.remove(exp)
            save_expenses(expenses)
            print("Expense deleted successfully.")
            return
    print("Error: Expense ID not found.")


# Summary of all expenses
def summary(month=None):
    expenses = load_expenses()
    total = sum(exp['amount'] for exp in expenses if month is None or int(exp['date'].split('-')[1]) == month)

    if month:
        print(f"Total expenses for month {month}: ${total}")
    else:
        print(f"Total expenses: ${total}")


# Main function to handle commands
def main():
    while True:
        command = input("$ expense-tracker ").strip().split()

        if command[0] == "add":
            description = command[3].strip('"')
            amount = float(command[5])
            add_expense(description, amount)

        elif command[0] == "list":
            list_expenses()

        elif command[0] == "delete":
            try:
                expense_id = int(command[3])
                delete_expense(expense_id)
            except ValueError:
                print("Error: Invalid ID.")

        elif command[0] == "summary":
            month = None
            if len(command) > 2 and command[2] == '--month':
                month = int(command[3])
            summary(month)

        elif command[0] == "exit":
            break

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
