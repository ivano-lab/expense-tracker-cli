import json
import os
from datetime import datetime

DATA_FILE = 'expenses.json'


# Load expenses from JSON file
def load_expenses():
    if not os.path.exists(DATA_FILE):
        save_expenses([])
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

    if not description:
        print("Error: Description cannot be empty.")
        return

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
    print("Expense added successfully.")

# List all expenses
def list_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses found.")
        return
    print(f"{'ID':<5} {'Date':<11} {'Description':<12} {'Amount':<7}")
    for exp in expenses:
        print(f"{exp['id']:<5} {exp['date']:<11} {exp['description']:<12} ${exp['amount']:.2f}")


# Delete an expense
def delete_expense(expense_id):
    expenses = load_expenses()
    if not expenses:
        print("Error: No expenses found.")
        return

    updated_expenses = [exp for exp in expenses if exp['id'] != expense_id]

    if len(updated_expenses) < len(expenses):
        save_expenses(updated_expenses)
        print("Expense deleted successfully.")
    else:
        print("Error: Expense ID not found.")

def summary():
    expenses = load_expenses()

    if not expenses:
        print("No expenses found.")
        return

    total = 0
    for exp in expenses:

        total += exp['amount']

    print(f"Total expenses: ${total:.2f}")


def summary_by_month(month):
    expenses = load_expenses()

    if not expenses:
        print("No expenses found.")
        return

    total = 0
    for exp in expenses:
        expense_month = int(exp['date'].split('-')[1])

        if expense_month == month:
            total += exp['amount']

    if total > 0:
        print(f"Total expenses for month {month}: ${total:.2f}")
    else:
        print(f"No expenses found for month {month}.")

# Main function to handle commands
def main():
    while True:
        command = input("$ expense-tracker ").strip().split()

        if command[0] == "add":

            if len(command) < 5:
                print(
                    "Error: Insufficient arguments for 'add'. Usage: add --description <description> --amount <amount>")
                continue

            try:
                description_index = command.index("--description") + 1
                amount_index = command.index("--amount") + 1

                description = command[description_index].strip('"')
                amount = float(command[amount_index])

                add_expense(description, amount)

            except (ValueError, IndexError) as e:
                print("Error while processing arguments:", e)

        elif command[0] == "list":
            list_expenses()

        elif command[0] == "delete":
            try:
                expense_id = int(command[2])
                delete_expense(expense_id)
            except ValueError:
                print("Error: Invalid ID. Must be a number")
            except IndexError:
                print("Error: ID not found")

        elif command[0] == "summary":
            month = None

            if len(command) > 2 and command[1] == '--month':
                try:
                    month = int(command[2])
                    if month < 1 or month > 12:
                        print("Error: Please enter a valid month between 1 and 12.")
                        continue
                except (ValueError, IndexError):
                    print("Error: Invalid month. Must be a number.")
                    continue

            if month is not None:
                summary_by_month(month)
            else:
                summary()

        elif command[0] == "exit":
                break

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
