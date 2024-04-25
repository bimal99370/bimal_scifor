import tkinter as tk
from math import *


def evaluate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))


def clear_entry():
    entry.delete(0, tk.END)


def create_button(root, text, row, col, colspan=1, rowspan=1, command=None):
    button = tk.Button(root, text=text, padx=20, pady=20, bg='#FFD700', command=command)
    button.grid(row=row, column=col, columnspan=colspan, rowspan=rowspan, sticky="nsew")
    return button


# Create the main window
root = tk.Tk()
root.title("Advanced Calculator")
root.configure(bg='#FFD700')  # Set background color to yellow

# Entry widget for displaying the expression and result
entry = tk.Entry(root, width=20, font=('Arial', 16), bd=5, insertwidth=4, justify="right")
entry.grid(row=0, column=0, columnspan=5, sticky="nsew")

# Buttons
numbers = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '0', '00', '%'
]

operators = [
    '/', '*', '-',
    '+', 'sin', 'cos',
    'tan', 'sqrt', '(',
    ')', 'CE', '='
]

# Add number buttons
row_val = 1
col_val = 0

for button in numbers:
    create_button(root, button, row_val, col_val, 1, 1, lambda val=button: button_click(val))
    col_val += 1
    if col_val > 2:
        col_val = 0
        row_val += 1

# Add operator buttons
row_val = 1
col_val = 3

for button in operators:
    if button == '=':
        create_button(root, button, row_val, col_val, 2, 1, evaluate_expression)
    elif button == 'CE':
        create_button(root, button, row_val, col_val, 1, 1, clear_entry)
    else:
        create_button(root, button, row_val, col_val, 1, 1, lambda val=button: button_click(val))

    col_val += 1
    if col_val > 4:
        col_val = 3
        row_val += 1

# Configure row and column weights to make buttons expandable
for i in range(7):
    root.grid_rowconfigure(i, weight=1)

# Increase weight of the last column to fill the space
root.grid_columnconfigure(5, weight=1)

# Run the Tkinter main loop
root.mainloop()
