#gui/error_dialog
import tkinter as tk
from tkinter import ttk

class ErrorDialog(tk.Toplevel):
    def __init__(self, parent, message):
        super().__init__(parent)
        self.title("Error")
        self.geometry("300x120")
        self.resizable(False, False)

        ttk.Label(self, text=message, wraplength=260).pack(pady=20)
        ttk.Button(self, text="OK", command=self.destroy).pack()