# Expense Tracker CLI

A command-line application to track personal expenses using SQLite. Supports adding, viewing, updating, and deleting expenses, along with category and monthly spending summaries.

## Features

- Add expenses with date, category, amount, and optional description
- View all recorded expenses
- Update or delete existing expenses by ID
- View a spending summary: total spent, category-wise breakdown, and monthly totals
- Input validation for dates, amounts, and categories
- Automated tests using pytest

## Tech Stack

- Python 3.13
- SQLite3 (built-in, no external database setup required)
- argparse (command-line interface)
- pytest (testing)

## Project Structure

expense-tracker-cli/
├── src/
│ ├── tracker.py # CLI entry point
│ ├── db.py # Database operations and validation
│ ├── models.py # Expense data model
│ └── reports.py # Summary and analysis functions
├── tests/
│ └── test_db.py # Automated tests for database functions
├── data/ # SQLite database (excluded from version control)
├── requirements.txt
└── README.md

## How to Run Locally

1. Clone the repository :

gitclonehttps://github.com/HarshitaSuchak11/expense-tracker-cli.git cdexpense-tracker-cli

2. Create and activate a virtual environment :python -m venv venv
   venv\Scripts\Activate.ps1
   (On Mac/Linux: `source venv/bin/activate`)

3. Install dependencies:

pip install -r requirements.txt

## Usage

**Add an expense:**

python src/tracker.py add --date 2026-09-01 --category Food --amount 250 --description "Lunch"

**View all expenses:**

python src/tracker.py view

**Update an expense:**

python src/tracker.py update --id 1 --amount 300

**Delete an expense:**

python src/tracker.py delete --id 1

**View spending summary:**

python src/tracker.py summary

##Running Tests

pytest

All core database operations (add, update, delete, and validation logic) are covered by automated tests using temporary, isolated test databases.

## Example Output

Total spent : Rs. 2100.00
Spending by category:
Food: Rs. 400.00 (19.0%)
Travel : Rs. 500.00(23.8%)
Shopping: Rs. 1200.00(57.1%)

Spending by month:
2026-09 : Rs. 900.00
2026-08: Rs. 1200.00

## What I'd Improve With More Time

- Add data export to CSV
- Add a visulaization command (bar chart of spending by category using matplotlib)
- Package the CLI so it can be installed and run as a proper command (`pip install -e .`)
- Add date-range filtering for the `view` comand

## What I learned

Building this project helped me understand database fundamentals (SQL, schema design), building a clean comand-line unterface with argpase, input validation and error handling, and writing automated tests with pytest and fixtures.


