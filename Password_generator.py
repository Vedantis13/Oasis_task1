#TASK-1 
#password generator task
import random
import string
import tkinter as tk
from tkinter import messagebox

# Function to generate password
def password_generate():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid positive integer for the length.")
        return

    include_uppercase = uppercase_var.get()
    include_lowercase = lowercase_var.get()
    include_digits = digits_var.get()
    include_symbols = symbols_var.get()
    characters = ''
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation
    if characters:
        password = ''.join(random.choice(characters) for i in range(length))
        result_label.config(text="Generated Password: " + password)
    else:
        messagebox.showwarning("Input Error", "Please select at least one character type.")

# GUI Setup
root = tk.Tk()
root.title("Creative Password Generator")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

title_label = tk.Label(root, text="Password Generator", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

tk.Label(root, text="Enter the length of password:", bg="#f0f0f0").pack()
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

uppercase_var = tk.BooleanVar()
lowercase_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Uppercase", variable=uppercase_var, bg="#f0f0f0").pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Lowercase", variable=lowercase_var, bg="#f0f0f0").pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Digits", variable=digits_var, bg="#f0f0f0").pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var, bg="#f0f0f0").pack(anchor='w', padx=20)

generate_button = tk.Button(root, text="Generate Password", command=password_generate, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
generate_button.pack(pady=10)

result_label = tk.Label(root, text="", bg="#f0f0f0", font=("Helvetica", 12))
result_label.pack(pady=10)

root.mainloop()
