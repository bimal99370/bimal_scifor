def currency_converter(amount, from_currency, to_currency):
    # Define exchange rates (as of a specific date)
    exchange_rates = {
        'USD': {
            'EUR': 0.85,
            'GBP': 0.73,
            'INR': 73.5,
            'ALL': 101.0,
            'AFN': 90.5,
            'ARS': 109.0,
            'AWG': 1.80,
            'AUD': 1.32,
            'AZN': 1.70,
            'BSD': 1.00,
            'BBD': 2.00,
            'BYN': 2.55,
            'BZD': 2.00,
            'BMD': 1.00,
            'BOB': 6.91,
            'BAM': 1.63,
            'BWP': 14.50,
            'BGN': 1.65,
            'BND': 1.35,
            'KHR': 4088.0,
            'CAD': 1.25,
            'KYD': 0.82,
            'CLP': 784.0,
            'CNY': 6.38,
            'COP': 4088.0,
            'CRC': 613.0,
            'HRK': 6.36,
            'CUP': 26.5,
            'CZK': 22.0,
            'DKK': 6.20,
            'DOP': 57.5,
            'XCD': 2.70,
            'EGP': 15.70,
            'SVC': 8.75,
            'FKP': 0.73,
            'FJD': 2.06,
            'GHS': 10.00,
            'GIP': 0.73,
            'GTQ': 7.68,
            'GGP': 0.73,
            'GYD': 209.0,
            'HNL': 24.5,
            'HKD': 7.75,
            'HUF': 294.0,
            'ISK': 135.0,
        },
        'EUR': {
            'USD': 1.18,
            'GBP': 0.86,
            'INR': 88.0,
            'ALL': 118.0,
            'AFN': 105.0,
            'ARS': 127.0,
            'AWG': 2.15,
            'AUD': 1.57,
            'AZN': 2.02,
            'BSD': 1.19,
            'BBD': 2.39,
            'BYN': 3.04,
            'BZD': 2.39,
            'BMD': 1.19,
            'BOB': 8.22,
            'BAM': 1.94,
            'BWP': 17.28,
            'BGN': 1.96,
            'BND': 1.59,
            'KHR': 4826.0,
            'CAD': 1.48,
            'KYD': 0.98,
            'CLP': 937.0,
            'CNY': 7.67,
            'COP': 4826.0,
            'CRC': 722.0,
            'HRK': 7.53,
            'CUP': 31.5,
            'CZK': 26.0,
            'DKK': 7.44,
            'DOP': 69.5,
            'XCD': 3.26,
            'EGP': 18.98,
            'SVC': 10.57,
            'FKP': 0.86,
            'FJD': 2.42,
            'GHS': 11.75,
            'GIP': 0.86,
            'GTQ': 9.05,
            'GGP': 0.86,
            'GYD': 245.0,
            'HNL': 28.87,
            'HKD': 9.14,
            'HUF': 348.0,
            'ISK': 160.0,
        },
        'GBP': {
            'USD': 1.37,
            'EUR': 1.16,
            'INR': 103.5,
            'ALL': 140.0,
            'AFN': 125.0,
            'ARS': 152.0,
            'AWG': 2.56,
            'AUD': 1.88,
            'AZN': 2.41,
            'BSD': 1.42,
            'BBD': 2.85,
            'BYN': 3.63,
            'BZD': 2.85,
            'BMD': 1.42,
            'BOB': 9.79,
            'BAM': 2.32,
            'BWP': 20.63,
            'BGN': 2.33,
            'BND': 1.89,
            'KHR': 5741.0,
            'CAD': 1.77,
            'KYD': 1.17,
            'CLP': 1120.0,
            'CNY': 9.17,
            'COP': 5741.0,
            'CRC': 860.0,
            'HRK': 8.96,
            'CUP': 37.5,
            'CZK': 31.0,
            'DKK': 8.85,
            'DOP': 82.75,
            'XCD': 3.88,
            'EGP': 22.65,
            'SVC': 12.60,
            'FKP': 1.16,
            'FJD': 3.26,
            'GHS': 15.75,
            'GIP': 1.16,
            'GTQ': 12.27,
            'GGP': 1.16,
            'GYD': 330.0,
            'HNL': 38.87,
            'HKD': 12.35,
            'HUF': 468.0,
            'ISK': 215.0,
        },
        # Add more currencies as needed
    }

    # Check if currencies are defined in exchange rates
    if from_currency not in exchange_rates or to_currency not in exchange_rates[from_currency]:
        print("Error: Unsupported currency pair.")
        return None

    # Convert the amount
    converted_amount = amount * exchange_rates[from_currency][to_currency]

    return converted_amount

# Example: Convert 100 USD to EUR
amount_to_convert = 100
from_currency = "USD"
to_currency = "EUR"
result = currency_converter(amount_to_convert, from_currency, to_currency)

if result is not None:
    print(f"{amount_to_convert} {from_currency} is equal to {result:.2f} {to_currency}")

import tkinter as tk
from tkinter import ttk

def currency_converter(amount, from_currency, to_currency):
# Replace this function with the currency_converter function from the previous code

# Tkinter App
class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")

        # Variables
        self.amount_var = tk.DoubleVar(value=0.0)
        self.from_currency_var = tk.StringVar(value="USD")
        self.to_currency_var = tk.StringVar(value="EUR")
        self.result_var = tk.StringVar(value="")

        # Entry Widgets
        self.amount_entry = ttk.Entry(root, textvariable=self.amount_var, width=10, font=('Arial', 12))
        self.amount_entry.grid(row=0, column=0, padx=10, pady=10)

        # Combobox for "From" currency
        self.from_currency_combobox = ttk.Combobox(root, textvariable=self.from_currency_var, values=list(exchange_rates.keys()))
        self.from_currency_combobox.grid(row=0, column=1, padx=10, pady=10)

        # Combobox for "To" currency
        self.to_currency_combobox = ttk.Combobox(root, textvariable=self.to_currency_var, values=list(exchange_rates.keys()))
        self.to_currency_combobox.grid(row=0, column=2, padx=10, pady=10)

        # Button to perform conversion
        self.convert_button = ttk.Button(root, text="Convert", command=self.convert_currency)
        self.convert_button.grid(row=1, column=0, columnspan=3, pady=10)

        # Result Label
        self.result_label = ttk.Label(root, textvariable=self.result_var, font=('Arial', 14, 'bold'))
        self.result_label.grid(row=2, column=0, columnspan=3, pady=10)

    def convert_currency(self):
        try:
            amount = float(self.amount_var.get())
            from_currency = self.from_currency_var.get()
            to_currency = self.to_currency_var.get()

            result = currency_converter(amount, from_currency, to_currency)

            if result is not None:
                self.result_var.set(f"{amount:.2f} {from_currency} is equal to {result:.2f} {to_currency}")
            else:
                self.result_var.set("Error converting currency.")
        except ValueError:
            self.result_var.set("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    # Create Tkinter window
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()
