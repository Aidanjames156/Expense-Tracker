﻿# Expense Tracker

A simple command-line expense tracking application that helps you manage and monitor your expenses.

## Features

- Add new expenses with descriptions and amounts
- Update existing expenses
- Delete expenses
- List all expenses in a formatted table
- View expense summaries (total or by month)

## Installation

1. Make sure you have Python installed on your system
2. Clone this repository or download the files
3. No additional dependencies required - uses only Python standard library

## Usage

### Basic Commands

```bash
# Add a new expense
python [expensetracker.py](http://_vscodecontentref_/1) add "description" amount
python [expensetracker.py](http://_vscodecontentref_/2) add "groceries" 50.75

# List all expenses
python [expensetracker.py](http://_vscodecontentref_/3) list

# View expense summary
python [expensetracker.py](http://_vscodecontentref_/4) summary          # All time total
python [expensetracker.py](http://_vscodecontentref_/5) summary 7        # July's total

# Update an expense
python [expensetracker.py](http://_vscodecontentref_/6) update ID amount
python [expensetracker.py](http://_vscodecontentref_/7) update 1 45.50

# Delete an expense
python [expensetracker.py](http://_vscodecontentref_/8) delete ID
python [expensetracker.py](http://_vscodecontentref_/9) delete 1
```
#Project URL
https://roadmap.sh/projects/expense-tracker
