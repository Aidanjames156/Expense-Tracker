import sys
import argparse
from datetime import datetime
import os
import json

JSON_FILE = "expenses.json"

def load_expenses():
    if not os.path.exists(JSON_FILE):
        return[]
    with open(JSON_FILE, "r") as f:
        return json.load(f)

def save_expenses(expenses):
    with open(JSON_FILE, "w") as f:
        json.dump(expenses, f, indent=2)

#Add expense with description and amount
def add_expense(description, amount):
    expenses = load_expenses()
    new_id = max([e["ID"] for e in expenses], default = 0) + 1
    date = datetime.now().isoformat()
    expense = {
        "ID": new_id,
        "Date": date,
        "description": description,
        "amount": amount
    }
    expenses.append(expense)
    save_expenses(expenses)
    print(f"Added expense: {description}")

#update expense
def update_expense(ID, amount):
    expenses = load_expenses()
    found = False
    for expense in expenses:
        if int(expense["ID"]) == int(ID):
            expense["amount"] = amount
            expense["Date"] = datetime.now().isoformat()  # Optionally update the date
            found = True
            break
    if found:
        save_expenses(expenses)
        print(f"Expense with ID {ID} updated to amount {amount}.")
    else:
        print(f"No expense found with ID {ID}.")

#delete expense
def delete_expense(ID):
    expenses = load_expenses()
    expenses = [expense for expense in expenses if int(expense["ID"]) != int(ID)]
    save_expenses(expenses)
    print(f"Expense with ID {ID} deleted.")

#View all expenses
def list_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses found.")
        return
    else:
        print("{:<4} {:<12} {:<15} {:<10}".format("ID", "Date", "Description", "Amount"))
        for expense in expenses:
            date = expense['Date'].split('T')[0]
            print("{:<4} {:<12} {:<15} ${:<9.2f}".format(
                expense['ID'],
                date,
                expense['description'],
                expense['amount']
            ))

#View summary
def summary_expenses(month=None):
    expenses = load_expenses()
    if not expenses:
        print("No expenses found.")
        return
    
    summary = 0
    current_year = datetime.now().year
    
    for expense in expenses:
        expense_date = datetime.fromisoformat(expense['Date'])
        if month:
            # If only month number is provided, use current year
            target_month = f"{current_year}-{int(month):02d}"
            if expense_date.strftime("%Y-%m") == target_month:
                summary += expense['amount']
        else:
            summary += expense['amount']
    
    if month:
        month_name = datetime.strptime(str(month), "%m").strftime("%B")
        print(f"# Total expenses for {month_name}: ${summary:.2f}")
    else:
        print(f"# Total expenses: ${summary:.2f}")

def main():
    parser = argparse.ArgumentParser(description="Expense Tracker")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Add subcommand
    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("description", help="Description of the expense")
    add_parser.add_argument("amount", type=float, help="Amount of the expense")

    # Update subcommand
    update_parser = subparsers.add_parser("update", help="Update an existing expense")
    update_parser.add_argument("ID", type=int, help="ID of expense to update")
    update_parser.add_argument("amount", type=float, help="New amount of the expense")

    # Delete subcommand
    delete_parser = subparsers.add_parser("delete", help="Delete an existing expense")
    delete_parser.add_argument("ID", type=int, help="ID of expense to update")

    # List subcommand
    list_parser = subparsers.add_parser("list", help="List all expenses")

    # Summary subcommand
    summary_parser = subparsers.add_parser("summary", help="View summary of expenses")
    summary_parser.add_argument("month", type=int, help="Month number (1-12)", nargs='?', default=None)

    args = parser.parse_args()

    if args.command == "add":
        add_expense(args.description, args.amount)
    elif args.command == "update":
        update_expense(args.ID, args.amount)
    elif args.command == "delete":
        delete_expense(args.ID)
    elif args.command == "list":
        list_expenses()
    elif args.command == "summary":
        summary_expenses(args.month)

if __name__ == "__main__":
    main()

