import tkinter as tk
from tkinter import messagebox


def register():
    name = entry_name.get()
    age = entry_age.get()
    gender = gender_var.get()
    address = entry_address.get("1.0", tk.END).strip()
    email = entry_email.get()
    contact_no = entry_contact.get()
    country = entry_country.get()
    state = entry_state.get()
    diseases = [disease_var.get() for disease_var in disease_vars]

    message = f"Registration Details:\n\nName: {name}\nAge: {age}\nGender: {gender}\nAddress: {address}\nEmail: {email}\nContact_No: {contact_no}\nCountry: {country}\nState: {state}\nDiseases: {diseases}"

    messagebox.showinfo("Registration Successful", message)

    # # You can add your logic here to process the form data as needed
    # print("Name:", name)
    # print("Age:", age)
    # print("Gender:", gender)
    # print("Address:", address)
    # print("Email:", email)
    # print("Contact No:", contact_no)
    # print("Country:", country)
    # print("State:", state)
    # print("Diseases:", diseases)

# Create main window
root = tk.Tk()
root.title("COVID Vaccine Registration Form")

# Add a heading
tk.Label(root, text="COVID Vaccine Registration Form", font=("Helvetica", 17, "bold"),background="blue",foreground="white").grid(row=0, column=0, columnspan=3, pady=10)

# Create and place form elements
tk.Label(root, text="Name of the visitor",font="Helvetica 10 bold italic",fg="darkblue").grid(row=1, column=0, padx=10, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Age of the visitor",font="Helvetica 10 bold italic",fg="darkblue").grid(row=2, column=0, padx=10, pady=5)
entry_age = tk.Entry(root)
entry_age.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Gender",font="Helvetica 10 bold italic",fg="darkblue").grid(row=3, column=0, padx=10, pady=5)
gender_var = tk.StringVar()
gender_var.set("Male")  # Default value
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").grid(row=3, column=1, padx=6, pady=5)
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").grid(row=3, column=2, padx=6, pady=5)

tk.Label(root, text="Address",font="Helvetica 10 bold italic",fg="darkblue").grid(row=4, column=0, padx=10, pady=5)
entry_address = tk.Text(root, height=3, width=30)
entry_address.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="Email Id",font="Helvetica 10 bold italic",fg="darkblue").grid(row=5, column=0, padx=10, pady=5)
entry_email = tk.Entry(root)
entry_email.grid(row=5, column=1, padx=10, pady=5)

tk.Label(root, text="Contact No",font="Helvetica 10 bold italic",fg="darkblue").grid(row=6, column=0, padx=10, pady=5)
entry_contact = tk.Entry(root)
entry_contact.grid(row=6, column=1, padx=10, pady=5)

tk.Label(root, text="Country",font="Helvetica 10 bold italic",fg="darkblue").grid(row=7, column=0, padx=10, pady=5)
entry_country = tk.Entry(root)
entry_country.grid(row=7, column=1, padx=10, pady=5)

tk.Label(root, text="State",font="Helvetica 10 bold italic",fg="darkblue").grid(row=8, column=0, padx=10, pady=5)
entry_state = tk.Entry(root)
entry_state.grid(row=8, column=1, padx=10, pady=5)

tk.Label(root, text="Select Diseases",font="Helvetica 10 bold italic",fg="darkblue").grid(row=10, column=0, padx=10, pady=5)
disease_vars = [tk.IntVar() for _ in range(4)]
disease_names = ["Cold", "Cough", "Fever", "Headache"]
for i, disease_name in enumerate(disease_names):
    tk.Checkbutton(root, text=disease_name, variable=disease_vars[i]).grid(row=10+i//2, column=1 + i % 2, sticky=tk.W, padx=11, pady=3)

# Register button
register_button = tk.Button(root, text="Register",font="comicsansms 12 bold ",fg="white",bg="darkblue", command=register)
register_button.grid(row=12, column=0, columnspan=4, pady=10)

# Start the main loop
root.maxsize(500,500)
root.minsize(500,500)
root.mainloop()
