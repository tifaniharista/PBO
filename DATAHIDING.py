import tkinter as tk
from tkinter import messagebox

class BankAccount: 
    def __init__(self):
        self.__balance = 0 # private atribute

    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount 
        else:
            raise ValueError("Invalid deposit amount!")
        
    def add_balance(self):
        try:
            amount = int(entry_amount.get())
            account.deposit(amount)
            label_balance.config(text=f"Balance: {account.get_balance()}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def reset_balance(self):
        """Reset balance to initial value and clear the input field."""
        self.__balance = 0
        label_balance.config(text=f"Balance: {self.get_balance()}")
        entry_amount.delete(0, tk.END)

#GUI TKINTER
root = tk.Tk()
root.title('Data Hiding in BankAccount')

account = BankAccount()

label_balance = tk.Label(root, text=f"Balance: {account.get_balance()}")
label_balance.pack()

entry_amount = tk.Entry(root)
entry_amount.pack()

button_deposit = tk.Button(root, text="Deposit", command=account.add_balance)
button_deposit.pack()

button_reset = tk.Button(root, text="Reset", command=account.reset_balance)
button_reset.pack(pady=10)

root.mainloop()