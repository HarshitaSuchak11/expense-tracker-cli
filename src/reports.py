import sys
import os 

sys.path.append(os.path.dirname(__file__))

import db 

#total spending
def total_spent():
    expenses = db.get_all_expenses()
    total = sum(row[3] for row in expenses)
    return total

#Category wise breakdown
def category_breakdown():
    expenses = db.get_all_expenses()
    breakdown = {}

    for row in expenses :
        category = row[2]
        amount = row[3]
        if category in breakdown:
            breakdown[category] += amount 
        else:
            breakdown[category] = amount 
    return breakdown 


#monthly total
def monthly_totals() :
    expenses = db.get_all_expenses()
    monthly ={}

    for row in expenses :
        date = row[1]
        amount = row[3]
        month = date[ :7] 

        if month in monthly :
            monthly[month] += amount
        else:
            monthly[month] = amount 
    return monthly 



def print_summary() :
    expenses = db.get_all_expenses();

    if not expenses :
        print("No expenses recorded yet. Add some using the 'add' command.")
        return 

    
    total = total_spent()
    categories = category_breakdown()
    months = monthly_totals() 

    print("\n Total spent: ", total)
    print ("\n Spending by category:")

    for category, amount in categories.items():
        percentage = (amount / total) * 100  if total > 0 else 0

        print(f"  {category}: ₹{amount:.2f} ({percentage:.1f}%)")

        print("\n Spending by month: ")
        for month, amount in months.items():
            print(f" {month}: Rs.{amount:.2f}")





