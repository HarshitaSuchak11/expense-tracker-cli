class Expense:
    def __init__(self, id, date, category, amount, description):
        self.id = id
        self.date = date
        self.category = category 
        self.amount = amount 
        self.description = description

    def __str__(self):
        return f"[{self.id}] {self.date} | {self.category} | {self.amount} | {self.description}"
    