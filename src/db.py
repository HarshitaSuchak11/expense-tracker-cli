import sqlite3
import os
from datetime import datetime 

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "expenses.db")


#Creation of table
def init_db() :
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            description TEXT
        )
    """)
    conn.commit()
    conn.close()


def validate_expense_data(date, category, amount) :
    errors =[]

    try :
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError :
        errors.append(f"Invalid date format : '{date}'. Use YYYY-MM-DD")

    if not category or not category.strip():
        errors.append("Category cannot be empty.")

    if amount is None or amount <= 0 :
        errors.append("Amount must be a positive number.")

    return errors

#Addition of Expenses
def add_expense(date, category, amount, description=""):

    errors = validate_expense_data(date, category, amount)
    if errors :
        for error in errors :
            print(f"Error : {error}")
        return False

    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO expenses (date, category, amount, description) VALUES (?,?,?,?)",
        (date, category, amount, description)
    )
    conn.commit()
    conn.close()
    print("Expense added successfully.")
    return True 

#View all expenses
def get_all_expenses():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses ORDER BY date DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows


#Deletion of an expenses
def delete_expense(expense_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    rows_affected = cursor.rowcount 
    conn.commit()
    conn.close()

    if rows_affected == 0:
        print(f"No expense found with ID {expense_id}")
        return False 
    else :
        print(f"Expense {expense_id} deleted.")
        return True 

    

#Update of expense
def update_expense(expense_id, date= None ,category = None ,amount = None , description = None) :
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM expenses WHERE id = ?", (expense_id,))
    if cursor.fetchone() is None:
        print(f"No expense with ID {expense_id}.")
        conn.close()
        return False 

    if date:
        try :
            datetime.strptime(date ,"%Y-%m-%d")
        except :
            print(f"Invalid date format : '{date}'. Use YYYY-MM-DD. Update cancelled.")
            conn.close()
            return False 
        
        cursor.execute("UPDATE expenses SET date = ? WHERE id = ?", (date, expense_id))
    if category:
        cursor.execute("UPDATE expenses SET category = ? WHERE id = ?", (category, expense_id))
    if amount is not None :
        if amount <= 0 :
            print("Amount must be positive. Update cancelled.")
            conn.close()
            return False 
        
        cursor.execute("UPDATE expenses SET amount = ? WHERE id =?", (amount, expense_id))
    if description is not None :
        cursor.execute("UPDATE expenses SET description = ? WHERE id =?", (description, expense_id))

    conn.commit()
    conn.close()
    print(f"Expense {expense_id} updated.")
    return True 

    