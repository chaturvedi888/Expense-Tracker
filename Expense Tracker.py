class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, item, amount):
        self.expenses.append((item, amount))
        print(f"Expense '{item}' of {amount} added successfully.")

    def view_expenses(self):
        if self.expenses:
            print("Your Expenses:")
            for item, amount in self.expenses:
                print(f"{item}: ${amount}")
        else:
            print("No expenses recorded yet.")

    def calculate_total_expenses(self):
        total = sum(amount for _, amount in self.expenses)
        print(f"Total expenses: ${total}")


def main():
    tracker = ExpenseTracker()
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total Expenses")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            item = input("Enter expense item: ")
            amount = float(input("Enter expense amount: "))
            tracker.add_expense(item, amount)
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            tracker.calculate_total_expenses()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")


if __name__ == "__main__":
    main()
