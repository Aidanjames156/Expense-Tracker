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

#delete expense

#View all expenses

#View summary

#View summary for month

def main():
    print(datetime.now())
    parser = argparse.ArgumentParser(description="Expense Tracker")
    parser.add_argument("description", help="Description of the expense")
    parser.add_argument("amount", type=float, help="Amount of the expense")
    args = parser.parse_args()

    add_expense(args.description, args.amount)

if __name__ == "__main__":
    main()

