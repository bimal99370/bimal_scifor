import tkinter as tk
from tkinter import ttk
from datetime import datetime

class BMIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")

        self.height_unit = tk.StringVar()
        self.height_unit.set("cm")

        self.weight_unit = tk.StringVar()
        self.weight_unit.set("kg")

        self.height_label = ttk.Label(root, text="Height:")
        self.height_entry = ttk.Entry(root)
        self.height_unit_option = ttk.OptionMenu(root, self.height_unit, "cm", "inches")

        self.weight_label = ttk.Label(root, text="Weight:")
        self.weight_entry = ttk.Entry(root)
        self.weight_unit_option = ttk.OptionMenu(root, self.weight_unit, "kg", "lbs")

        self.calculate_button = ttk.Button(root, text="Calculate BMI", command=self.calculate_bmi)

        self.bmi_scale = ttk.Scale(root, from_=10, to=40, orient=tk.HORIZONTAL, length=200, command=self.update_bmi)

        self.result_label = ttk.Label(root, text="BMI Report: ")
        self.result_value = tk.StringVar()
        self.result_display = ttk.Label(root, textvariable=self.result_value)

        self.save_button = ttk.Button(root, text="Save Data", command=self.save_data)

        self.height_label.grid(row=0, column=0, padx=10, pady=10)
        self.height_entry.grid(row=0, column=1, padx=10, pady=10)
        self.height_unit_option.grid(row=0, column=2, padx=10, pady=10)

        self.weight_label.grid(row=1, column=0, padx=10, pady=10)
        self.weight_entry.grid(row=1, column=1, padx=10, pady=10)
        self.weight_unit_option.grid(row=1, column=2, padx=10, pady=10)

        self.calculate_button.grid(row=2, column=0, columnspan=3, pady=10)

        self.bmi_scale.grid(row=3, column=0, columnspan=3, pady=10)

        self.result_label.grid(row=4, column=0, padx=10, pady=10)
        self.result_display.grid(row=4, column=1, columnspan=2, padx=10, pady=10)

        self.save_button.grid(row=5, column=0, columnspan=3, pady=10)

    def calculate_bmi(self):
        try:
            height = float(self.height_entry.get())
            weight = float(self.weight_entry.get())

            if self.height_unit.get() == "inches":
                height *= 2.54  # convert inches to centimeters

            if self.weight_unit.get() == "lbs":
                weight *= 0.453592  # convert pounds to kilograms

            bmi = weight / ((height / 100) ** 2)
            self.bmi_scale.set(bmi)

            if bmi < 18.5:
                self.result_value.set("Underweight")
                self.result_display.config(foreground="red")
            elif 18.5 <= bmi < 25:
                self.result_value.set("Normal")
                self.result_display.config(foreground="green")
            else:
                self.result_value.set("Overweight")
                self.result_display.config(foreground="red")

        except ValueError:
            self.result_value.set("Invalid Input")
            self.result_display.config(foreground="black")

    def update_bmi(self, value):
        self.result_value.set(f"BMI: {value}")

    def save_data(self):
        try:
            height = float(self.height_entry.get())
            weight = float(self.weight_entry.get())
            bmi = self.bmi_scale.get()

            with open("bmi_data.txt", "a") as file:
                now = datetime.now()
                date_time = now.strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"Date: {date_time}, Height: {height}, Weight: {weight}, BMI: {bmi}\n")

        except ValueError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = BMIApp(root)
    root.mainloop()
