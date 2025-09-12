import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Warning", "Password length should be at least 4.")
            return
        
        letters = string.ascii_letters
        digits = string.digits
        symbols = string.punctuation
        all_chars = letters + digits + symbols
        
        password = ''.join(random.choice(all_chars) for _ in range(length))
        password_var.set(password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

def copy_to_clipboard():
    password = password_var.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy!")

# GUI setup
root = tk.Tk()
root.title("🔐 Password Generator")
root.geometry("400x200")
root.resizable(False, False)

tk.Label(root, text="Enter password length:", font=("Arial", 12)).pack(pady=10)
length_entry = tk.Entry(root, font=("Arial", 14), justify="center")
length_entry.pack()

tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 12), bg="#4CAF50", fg="white").pack(pady=10)

password_var = tk.StringVar()
password_display = tk.Entry(root, textvariable=password_var, font=("Arial", 14), justify="center", width=30)
password_display.pack()

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, font=("Arial", 12), bg="#2196F3", fg="white").pack(pady=10)

root.mainloop()