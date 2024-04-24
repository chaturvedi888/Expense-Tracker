import tkinter as tk
from tkinter import messagebox

class ExpenseTrackerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Expense Tracker")
        self.expenses = []

        # Expense Entry Frame
        self.expense_frame = tk.Frame(master)
        self.expense_frame.pack(pady=10)

        self.item_label = tk.Label(self.expense_frame, text="Expense Item:")
        self.item_label.grid(row=0, column=0, padx=10)
        self.item_entry = tk.Entry(self.expense_frame)
        self.item_entry.grid(row=0, column=1)

        self.amount_label = tk.Label(self.expense_frame, text="Expense Amount:")
        self.amount_label.grid(row=1, column=0, padx=10)
        self.amount_entry = tk.Entry(self.expense_frame)
        self.amount_entry.grid(row=1, column=1)

        self.add_button = tk.Button(self.expense_frame, text="Add Expense", command=self.add_expense)
        self.add_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Expense Display Frame
        self.display_frame = tk.Frame(master)
        self.display_frame.pack(pady=10)

        self.expenses_label = tk.Label(self.display_frame, text="Your Expenses:")
        self.expenses_label.grid(row=0, column=0)

        self.expenses_text = tk.Text(self.display_frame, width=40, height=10)
        self.expenses_text.grid(row=1, column=0)

    def add_expense(self):
        item = self.item_entry.get()
        amount = self.amount_entry.get()
        if item and amount:
            try:
                amount = float(amount)
                self.expenses.append((item, amount))
                self.expenses_text.insert(tk.END, f"{item}: ${amount}\n")
                messagebox.showinfo("Success", f"Expense '{item}' of {amount} added successfully.")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid amount.")
        else:
            messagebox.showerror("Error", "Please enter both item and amount.")

def main():
    root = tk.Tk()
    app = ExpenseTrackerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
