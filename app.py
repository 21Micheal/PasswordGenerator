import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def generate_password():
    length = int(length_entry.get())
    use_upper = upper_var.get()
    use_lower = lower_var.get()
    use_digits = digit_var.get()
    use_special = special_var.get()
    
    char_pool = ""
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_lower:
        char_pool += string.ascii_lowercase
    if use_digits:
        char_pool += string.digits
    if use_special:
        char_pool += string.punctuation
    
    if not char_pool:
        messagebox.showwarning("Warning", "Please select at least one character set!")
        return
    
    password = ''.join(random.choice(char_pool) for _ in range(length))
    password_var.set(password)

def copy_to_clipboard():
    pyperclip.copy(password_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI Setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x400")
root.resizable(False, False)

# Title Label
title_label = tk.Label(root, text="Password Generator", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Length Input
length_frame = tk.Frame(root)
length_frame.pack(pady=5)
tk.Label(length_frame, text="Password Length:").pack(side=tk.LEFT)
length_entry = tk.Entry(length_frame, width=5)
length_entry.insert(0, "12")  # Default length
length_entry.pack(side=tk.LEFT)

# Options
tk.Label(root, text="Character Options:").pack()
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digit_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=False)

tk.Checkbutton(root, text="Uppercase (A-Z)", variable=upper_var).pack()
tk.Checkbutton(root, text="Lowercase (a-z)", variable=lower_var).pack()
tk.Checkbutton(root, text="Digits (0-9)", variable=digit_var).pack()
tk.Checkbutton(root, text="Special (!@#$)", variable=special_var).pack()

# Generate Button
password_var = tk.StringVar()
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

# Password Output
password_entry = tk.Entry(root, textvariable=password_var, font=("Arial", 14), width=25, justify="center", state="readonly")
password_entry.pack(pady=5)

# Copy Button
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=5)

# Run Application
root.mainloop()
