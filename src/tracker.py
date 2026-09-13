import argparse
import sys
import os 

sys.path.append(os.path.dirname(__file__))

import db 
import reports 

#argument parser set up
def main():
    parser = argparse.ArgumentParser(description="A simple CLI expense tracker")
    subparsers = parser.add_subparsers(dest = "command")
    export_parser = subparsers.add_parser("export", help="Export expenses to a CSV file")
    export_parser.add_argument("--filename", default="expenses_export.csv", help="Output CSV filename")
    chart_parser = subparsers.add_parser("chart", help="Generate a bar chart of spending by category")
#add command
    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("--date", required=True, help="Date in YYYY-MM-DD format")
    add_parser.add_argument("--category", required =True, help="Expense in category")
    add_parser.add_argument("--amount", required =True, type = float, help ="Amount spent")
    add_parser.add_argument("--description", default="", help="Optional description")

#view command
    view_parser = subparsers.add_parser("view", help = "View all expenses")

#delete comand
    delete_parser = subparsers.add_parser("delete", help = "Delete an expense by ID")
    delete_parser.add_argument("--id", required =True, type = int, help="ID of the expense to delete")

#update command
    update_parser = subparsers.add_parser("update", help ="Update an existing expense")
    update_parser.add_argument("--id", required = True, type= int, help="ID of the expense")
    update_parser.add_argument("--date", help ="new date")
    update_parser.add_argument("--category", help="New date")
    update_parser.add_argument("--amount", type = float, help ="New amount")
    update_parser.add_argument("--description", help ="New descriptionn")

# summay command
    summary_parser = subparsers.add_parser("summary", help="View spending summary and analysis")


    args = parser.parse_args()
    db.init_db()

    if args.command == "add":
        db.add_expense(args.date, args.category, args.amount, args.description)

    elif args.command == "view" :
        expenses = db.get_all_expenses()
        if not expenses:
            print("No expenses recorded yet.")
        for row in expenses:
            print(row)

    elif args.command == "delete" :
        db.delete_expense(args.id)
    elif args.command == "update" :
        db.update_expense(args.id, args.date, args.category, args.amount, args.description)
    elif args.command == "summary" :
        reports.print_summary()
    elif args.command == "export":
        reports.export_to_csv(args.filename)
    elif args.command == "chart" :
        reports.generate_category_chart()
        
    else:
        parser.print_help()


if __name__ =="__main__" :
    main()
        

