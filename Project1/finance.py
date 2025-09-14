import json
from datetime import datetime

class Transaction:
    def __init__(self, amount: float, category: str, date: str = None):
        self.amount = amount
        self.category = category
        self.date = date if date else datetime.now().strftime("%Y-%m-%d")

    def to_dict(self):
        return {"amount": self.amount, "category": self.category, "date": self.date}


class Income(Transaction):
    pass  # Inherits from Transaction


class Expense(Transaction):
    pass  # Inherits from Transaction


class Ledger:
    def __init__(self, filename="transactions.json"):
        self.filename = filename
        self.transactions = self.load_transactions()

    def add_transaction(self, transaction: Transaction):
        self.transactions.append(transaction.to_dict())
        self.save_transactions()

    def save_transactions(self):
        with open(self.filename, "w") as f:
            json.dump(self.transactions, f, indent=4)

    def load_transactions(self):
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def view_transactions(self):
        if not self.transactions:
            print("No transactions found.")
            return
        for t in self.transactions:
            print(f"{t['date']} | {t['category']} | {t['amount']}")

    def summary(self):
        income = sum(t["amount"] for t in self.transactions if t["amount"] > 0)
        expense = sum(-t["amount"] for t in self.transactions if t["amount"] < 0)
        balance = income - expense
        print(f"Total Income: {income}")
        print(f"Total Expenses: {expense}")
        print(f"Net Balance: {balance}")
