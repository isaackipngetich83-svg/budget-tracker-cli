# Budget Tracker CLI

A lightweight, command-line budget management tool that tracks income and expenses with persistent storage via JSON files.

## Features
- **Add Transactions:** Log income and expenses with categories.
- **List Transactions:** View a formatted table of all recorded data.
- **Summary:** Get an instant calculation of your balance.
- **Delete:** Remove specific transactions by ID.

## Installation
1. Clone the repository: `git clone https://github.com/isaackipngetich83-svg/budget-tracker-cli.git`
2. Ensure you have Python installed.
3. Run the application: `python budget.py --help`

## Usage Examples
- Add an expense: `python budget.py add --type expense --amount 20 --cat Food`
- List everything: `python budget.py list`
- Check balance: `python budget.py summary`
- Delete an item: `python budget.py delete --id 1`
