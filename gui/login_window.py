import tkinter as tk
from tkinter import ttk, messagebox
from models.database import Database
from gui.main_window import MainWindow


class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Payroll Login")
        self.geometry("340x260")
        self.configure(bg="#f4f6f8")  # light background
        self.db = Database()
        self.create_widgets()

    def create_widgets(self):
        # --- Title ---
        tk.Label(
            self,
            text="ABC Company Payroll System",
            font=("Arial", 14, "bold"),
            fg="#303030",
            bg="#f4f6f8"
        ).pack(pady=(10, 5))

        # --- Instruction Box ---
        instruction = (
            "Demo Login Credentials\n"
            "User ID: HR0001\n"
            "Password: adminpass"
        )

        tk.Label(
            self,
            text=instruction,
            justify="center",
            font=("Arial", 9),
            fg="#555555",
            bg="#e9edf2",
        ).pack(pady=8)

        # --- User ID ---
        tk.Label(
            self,
            text="User ID",
            bg="#f4f6f8"
        ).pack(pady=(6, 0))

        self.user_entry = ttk.Entry(self)
        self.user_entry.pack(pady=4)

        # --- Password ---
        tk.Label(
            self,
            text="Password",
            bg="#f4f6f8"
        ).pack(pady=(6, 0))

        self.pass_entry = ttk.Entry(self, show="*")
        self.pass_entry.pack(pady=4)

        # --- Login Button ---
        tk.Button(
            self,
            text="Login",
            bg="#1f8f3f",
            fg="white",
            font=("Arial", 10, "bold"),
            width=15,
            command=self.login
        ).pack(pady=14)

    def login(self):
        uid = self.user_entry.get()
        pwd = self.pass_entry.get()

        if uid == "HR0001" and pwd == "adminpass":
            self.destroy()
            app = MainWindow()
            app.mainloop()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials")
