import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_random_string(length, include_numbers=True, include_characters=True):
    characters = string.ascii_letters
    if include_numbers:
        characters += string.digits
        if not any(c.isdigit() for c in characters):
            characters += random.choice(string.digits)

    if include_characters:
        characters += string.punctuation
        if not any(c in string.punctuation for c in characters):
            characters += random.choice(string.punctuation)

    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def generate_password():
    try:
        length = int(length_entry.get())
        include_numbers = include_numbers_var.get()
        include_characters = include_characters_var.get()

        if length <= 0:
            messagebox.showerror("Error", "Password length must be greater than 0.")
            return

        result = generate_random_string(length, include_numbers, include_characters)
        result_label.config(text="Generated Password: " + result)
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid password length.")


root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x300")


title_label = tk.Label(root, text="Random Password Generator", font=("Helvetica", 14, "bold"))
title_label.pack(pady=10)

length_label = tk.Label(root, text="Password Length:")
length_label.pack()

length_entry = tk.Entry(root, width=40)
length_entry.pack(pady=5)

include_numbers_var = tk.BooleanVar()
include_numbers_check = tk.Checkbutton(root, text="Include Numbers", variable=include_numbers_var)
include_numbers_check.pack()

include_characters_var = tk.BooleanVar()
include_characters_check = tk.Checkbutton(root, text="Include Special Characters", variable=include_characters_var)
include_characters_check.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white")
generate_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack()

root.mainloop()
