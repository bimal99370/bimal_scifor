import tkinter as tk
import random

# Sample list of names
names = ['bimal', 'hari', 'ram', 'krishna', 'bhim']
completed_names = []

# Function to pick a random name from the list
def pick_name():
    if names:
        selected_name = random.choice(names)
        names.remove(selected_name)
        completed_names.append(selected_name)
        selected_name_label.config(text=selected_name)
        completed_names_label.config(text='\n'.join(completed_names))
        available_names_label.config(text='\n'.join(names))
    else:
        selected_name_label.config(text="All names have been picked")

# Function to select a specific name from the list
def select_name():
    if entry_field.get() in names:
        selected_name = entry_field.get()
        names.remove(selected_name)
        completed_names.append(selected_name)
        selected_name_label.config(text=selected_name)
        completed_names_label.config(text='\n'.join(completed_names))
        available_names_label.config(text='\n'.join(names))
    else:
        selected_name_label.config(text="Name not found in the list")

# Create the main window
root = tk.Tk()
root.title("Random Name Selector")
root.configure(bg='light blue')

# Create labels and buttons
tk.Label(root, text="Selected name", bg='light blue').grid(row=0, column=0)
selected_name_label = tk.Label(root, text="", bg='light blue')
selected_name_label.grid(row=1, column=0)

entry_field = tk.Entry(root)
entry_field.grid(row=2, column=0)
tk.Button(root, text="Select", command=select_name, bg='light green').grid(row=3, column=0)

tk.Button(root, text="Shuffle", command=pick_name, bg='light green').grid(row=4, column=0)

tk.Label(root, text="Already Selected", bg='light blue').grid(row=0, column=1)
completed_names_label = tk.Label(root, text="", bg='light blue')
completed_names_label.grid(row=1, column=1)

tk.Label(root, text="Available Names", bg='light blue').grid(row=2, column=1)
available_names_label = tk.Label(root, text='\n'.join(names), bg='light blue')
available_names_label.grid(row=3, column=1, rowspan=2)

# Run the application loop
root.mainloop()
