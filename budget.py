import argparse
import json
import os
from datetime import datetime

DATA_FILE = "data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    parser = argparse.ArgumentParser(description="Budget Tracker CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Add
    add = subparsers.add_parser("add")
    add.add_argument("--type", choices=["income", "expense"], required=True)
    add.add_argument("--amount", type=float, required=True)
    add.add_argument("--cat", required=True)

    # List
    subparsers.add_parser("list")

    # Summary
    subparsers.add_parser("summary")

    # Delete
    delete = subparsers.add_parser("delete")
    delete.add_argument("--id", type=int, required=True)

    args = parser.parse_args()
    data = load_data()

    if args.command == "add":
        entry = {"date": datetime.now().strftime("%Y-%m-%d"), "type": args.type, "amount": args.amount, "category": args.cat}
        data.append(entry)
        save_data(data)
        print(f"Added {args.type} of ${args.amount} in {args.cat}.")

    elif args.command == "list":
        if not data: print("No transactions.")
        else:
            print(f"{'ID':<4} | {'Date':<12} | {'Type':<8} | {'Amount':<10} | {'Category'}")
            for i, item in enumerate(data, 1):
                print(f"{i:<4} | {item['date']:<12} | {item['type']:<8} | ${item['amount']:<9.2f} | {item['category']}")

    elif args.command == "summary":
        income = sum(item['amount'] for item in data if item['type'] == 'income')
        expense = sum(item['amount'] for item in data if item['type'] == 'expense')
        print(f"Income: ${income:.2f} | Expenses: ${expense:.2f} | Balance: ${income - expense:.2f}")

    elif args.command == "delete":
        if 1 <= args.id <= len(data):
            removed = data.pop(args.id - 1)
            save_data(data)
            print(f"Deleted transaction: {removed['category']} (${removed['amount']})")
        else:
            print("Invalid ID.")

if __name__ == "__main__":
    main()