import requests
import random
import tkinter as tk

window = tk.Tk()
window.title("Random Quote Generator")
label = tk.Label(window, text=" ")
label.pack(pady=10)


def get_quote():
    response = requests.get("https://api.quotable.io/random")
    data = response.json()
    return data["content"]


def show_quote():
    quotes = get_quote()
    label.config(text=quotes)
    button1.pack()


button1 = tk.Button(window, text=" CLICK TO GET A RANDOM QUOTE", command=show_quote)
button1.pack()

window.mainloop()
