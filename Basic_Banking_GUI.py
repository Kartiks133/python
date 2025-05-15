import tkinter as tk
from tkinter import messagebox, simpledialog
import random
from datetime import datetime

class Bank_Of_404_Brain_Not_Found:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Bank App")
        self.root.geometry("500x400")

        self.admin_id = "admin404"
        self.admin_password = "password"
        self.accounts = []  # List to store account dictionaries
        self.current_user = None  # Tracks the logged-in user

        tk.Label(root, text="Simple Bank", font=("Arial", 16, "bold")).pack(pady=10)

        # Buttons for functionalities
        tk.Button(root, text="Admin Login", command=self.admin_login, width=20).pack(pady=10)
        tk.Button(root, text="User Login", command=self.user_login, width=20).pack(pady=10)
        tk.Button(root, text="Exit", command=root.quit, width=20).pack(pady=10)

    def admin_login(self):
        admin_window = tk.Toplevel(self.root)
        admin_window.title("Admin Login")
        admin_window.geometry("300x200")

        tk.Label(admin_window, text="Admin ID:").pack(pady=5)
        admin_id_entry = tk.Entry(admin_window)
        admin_id_entry.pack(pady=5)

        tk.Label(admin_window, text="Password:").pack(pady=5)
        admin_password_entry = tk.Entry(admin_window, show="*")
        admin_password_entry.pack(pady=5)

        def verify_admin():
            if (admin_id_entry.get() == self.admin_id and
                admin_password_entry.get() == self.admin_password):
                messagebox.showinfo("Success", "Admin login successful!")
                admin_window.destroy()
                self.admin_panel()
            else:
                messagebox.showerror("Error", "Invalid Admin ID or Password")

        tk.Button(admin_window, text="Login", command=verify_admin).pack(pady=10)

    def admin_panel(self):
        panel = tk.Toplevel(self.root)
        panel.title("Admin Panel")
        panel.geometry("400x400")

        tk.Label(panel, text="Admin Panel", font=("Arial", 14, "bold")).pack(pady=10)

        def view_accounts():
            if not self.accounts:
                messagebox.showinfo("Accounts", "No accounts found.")
            else:
                details = "".join([
                    f"Account {idx+1} - Name: {acc['name']}, Acc#: {acc['account_number']}, Balance: {acc['balance']}\n"
                    for idx, acc in enumerate(self.accounts)
                ])
                messagebox.showinfo("All Accounts", details)

        def add_account():
            if len(self.accounts) >= 5:
                messagebox.showerror("Error", "Cannot add more than 5 accounts!")
                return
            self.open_account()

        def remove_account():
            acc_number = simpledialog.askinteger("Remove Account", "Enter Account Number:")
            for acc in self.accounts:
                if acc["account_number"] == acc_number:
                    self.accounts.remove(acc)
                    messagebox.showinfo("Success", f"Account {acc_number} removed successfully!")
                    return
            messagebox.showerror("Error", "Account not found!")

        tk.Button(panel, text="View All Accounts", command=view_accounts).pack(pady=10)
        tk.Button(panel, text="Add Account", command=add_account).pack(pady=10)
        tk.Button(panel, text="Remove Account", command=remove_account).pack(pady=10)

    def user_login(self):
        if not self.accounts:
            messagebox.showerror("Error", "No accounts available! Admin must create accounts first.")
            return

        login_window = tk.Toplevel(self.root)
        login_window.title("User Login")
        login_window.geometry("300x200")

        tk.Label(login_window, text="Account Number:").pack(pady=5)
        acc_entry = tk.Entry(login_window)
        acc_entry.pack(pady=5)

        def verify_user():
            acc_number = acc_entry.get()
            if not acc_number.isdigit():
                messagebox.showerror("Error", "Invalid account number!")
                return
            acc_number = int(acc_number)
            for acc in self.accounts:
                if acc["account_number"] == acc_number:
                    self.current_user = acc
                    messagebox.showinfo("Success", "User login successful!")
                    login_window.destroy()
                    self.user_panel()
                    return
            messagebox.showerror("Error", "Account not found!")

        tk.Button(login_window, text="Login", command=verify_user).pack(pady=10)

    def user_panel(self):
        panel = tk.Toplevel(self.root)
        panel.title("User Panel")
        panel.geometry("400x300")

        tk.Label(panel, text=f"Welcome, {self.current_user['name']}!", font=("Arial", 14, "bold")).pack(pady=10)

        def deposit():
            amount = simpledialog.askinteger("Deposit", "Enter amount to deposit:")
            if amount and amount > 0:
                self.current_user["balance"] += amount
                messagebox.showinfo("Success", f"Deposited {amount} successfully!")
            else:
                messagebox.showerror("Error", "Invalid amount!")

        def withdraw():
            amount = simpledialog.askinteger("Withdraw", "Enter amount to withdraw:")
            if amount and amount > 0:
                if self.current_user["balance"] - amount < 500:
                    messagebox.showerror("Error", "Insufficient balance! Minimum 500 required.")
                else:
                    self.current_user["balance"] -= amount
                    messagebox.showinfo("Success", f"Withdrawn {amount} successfully!")
            else:
                messagebox.showerror("Error", "Invalid amount!")

        def view_account():
            details = (
                f"Name: {self.current_user['name']}\n"
                f"Account Number: {self.current_user['account_number']}\n"
                f"Balance: {self.current_user['balance']}\n"
            )
            messagebox.showinfo("Account Details", details)

        tk.Button(panel, text="Deposit Money", command=deposit).pack(pady=10)
        tk.Button(panel, text="Withdraw Money", command=withdraw).pack(pady=10)
        tk.Button(panel, text="View Account", command=view_account).pack(pady=10)

    def open_account(self):
        def create_account():
            name = name_entry.get()
            dob = dob_entry.get()
            aadhaar = aadhaar_entry.get()
            phone = phone_entry.get()

            # Validate inputs
            if not name or not dob or not aadhaar or not phone:
                messagebox.showerror("Error", "All fields are required!")
                return
            try:
                datetime.strptime(dob, "%d/%m/%Y")
            except ValueError:
                messagebox.showerror("Error", "DOB must be in DD/MM/YYYY format!")
                return
            if len(aadhaar) != 12 or not aadhaar.isdigit():
                messagebox.showerror("Error", "Aadhaar must be a 12-digit number!")
                return
            if len(phone) != 10 or not phone.isdigit():
                messagebox.showerror("Error", "Phone number must be a 10-digit number!")
                return

            # Create account
            new_account = {
                "name": name,
                "dob": dob,
                "aadhaar": aadhaar,
                "phone": phone,
                "balance": 500,
                "account_number": random.randint(1000000000, 9999999999)
            }
            self.accounts.append(new_account)
            messagebox.showinfo("Success", f"Account created! Account Number: {new_account['account_number']}")
            open_window.destroy()

        open_window = tk.Toplevel(self.root)
        open_window.title("Open Account")
        open_window.geometry("400x300")

        tk.Label(open_window, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        name_entry = tk.Entry(open_window)
        name_entry.grid(row=0, column=1)

        tk.Label(open_window, text="DOB (DD/MM/YYYY):").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        dob_entry = tk.Entry(open_window)
        dob_entry.grid(row=1, column=1)

        tk.Label(open_window, text="Aadhaar:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        aadhaar_entry = tk.Entry(open_window)
        aadhaar_entry.grid(row=2, column=1)

        tk.Label(open_window, text="Phone:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        phone_entry = tk.Entry(open_window)
        phone_entry.grid(row=3, column=1)

        tk.Button(open_window, text="Create Account", command=create_account).grid(row=4, column=0, columnspan=2, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = Bank_Of_404_Brain_Not_Found(root)
    root.mainloop()

