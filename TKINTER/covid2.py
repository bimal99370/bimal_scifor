import tkinter as tk
from tkinter import ttk


def submit_form():
    # Get values from the entries and widgets
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    address = address_text.get("1.0", "end-1c")
    email = email_entry.get()
    contact_no = contact_entry.get()
    country = country_entry.get()
    state = state_entry.get()
    diseases = [cold_var.get(), cough_var.get(), fever_var.get(), headache_var.get()]

    # Display the submitted information (you can modify this part)
    print("Name:", name)
    print("Age:", age)
    print("Gender:", gender)
    print("Address:", address)
    print("Email:", email)
    print("Contact No:", contact_no)
    print("Country:", country)
    print("State:", state)
    print("Selected Diseases:", [disease for disease in diseases if disease])

# Create the main window
root = tk.Tk()
root.title("COVID Vaccine Registration Form")

# Add a heading
heading_label = ttk.Label(root, text="COVID Vaccine Registration Form", font=("Helvetica", 17, "bold"),background="blue",foreground="white")
heading_label.grid(row=0, column=0, columnspan=3, pady=10)

# Create and place the form elements
name_label = ttk.Label(root, text="Name of the visitor:",foreground="blue",font=("Helvetica", 10, "bold"))
name_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
name_entry = ttk.Entry(root)
name_entry.grid(row=1, column=1, padx=10, pady=5)

age_label = ttk.Label(root, text="Age of the visitor:",foreground="blue",font=("Helvetica", 10, "bold"))
age_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
age_entry = ttk.Entry(root)
age_entry.grid(row=2, column=1, padx=10, pady=5)

gender_label = ttk.Label(root, text="Gender:",foreground="blue",font=("Helvetica", 10, "bold"))
gender_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
gender_var = tk.StringVar()
gender_radio_male = ttk.Radiobutton(root, text="Male", variable=gender_var, value="Male")
gender_radio_female = ttk.Radiobutton(root, text="Female", variable=gender_var, value="Female")
gender_radio_male.grid(row=3, column=1, padx=10, pady=5, sticky="w")
gender_radio_female.grid(row=3, column=2, padx=10, pady=5, sticky="w")

address_label = ttk.Label(root, text="Address:",foreground="blue",font=("Helvetica", 10, "bold"))
address_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
address_text = tk.Text(root, height=3, width=30)
address_text.grid(row=4, column=1, padx=10, pady=5)

email_label = ttk.Label(root, text="Email Id:",foreground="blue",font=("Helvetica", 10, "bold"))
email_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")
email_entry = ttk.Entry(root)
email_entry.grid(row=5, column=1, padx=10, pady=5)

contact_label = ttk.Label(root, text="Contact No:",foreground="blue",font=("Helvetica", 10, "bold"))
contact_label.grid(row=6, column=0, padx=10, pady=5, sticky="w")
contact_entry = ttk.Entry(root)
contact_entry.grid(row=6, column=1, padx=10, pady=5)

country_label = ttk.Label(root, text="Country:",foreground="blue",font=("Helvetica", 10, "bold"))
country_label.grid(row=7, column=0, padx=10, pady=5, sticky="w")
country_entry = ttk.Entry(root)
country_entry.grid(row=7, column=1, padx=10, pady=5)

state_label = ttk.Label(root, text="State:",foreground="blue",font=("Helvetica", 10, "bold"))
state_label.grid(row=8, column=0, padx=10, pady=5, sticky="w")
state_entry = ttk.Entry(root)
state_entry.grid(row=8, column=1, padx=10, pady=5)

diseases_label = ttk.Label(root, text="Select any diseases:",foreground="blue",font=("Helvetica", 10, "bold"))
diseases_label.grid(row=9, column=0, padx=10, pady=5, sticky="w")
cold_var = tk.BooleanVar()
cough_var = tk.BooleanVar()
fever_var = tk.BooleanVar()
headache_var = tk.BooleanVar()

cold_checkbox = ttk.Checkbutton(root, text="Cold", variable=cold_var)
cough_checkbox = ttk.Checkbutton(root, text="Cough", variable=cough_var)
fever_checkbox = ttk.Checkbutton(root, text="Fever", variable=fever_var)
headache_checkbox = ttk.Checkbutton(root, text="Headache", variable=headache_var)

cold_checkbox.grid(row=9, column=1, padx=10, pady=5, sticky="w")
cough_checkbox.grid(row=9, column=2, padx=10, pady=5, sticky="w")
fever_checkbox.grid(row=10, column=1, padx=10, pady=5, sticky="w")
headache_checkbox.grid(row=10, column=2, padx=10, pady=5, sticky="w")

submit_button = ttk.Button(root, text="REGISTER HERE", command=submit_form)
submit_button.grid(row=11, column=0, columnspan=3, pady=10)

# Run the main loop
root.mainloop()
