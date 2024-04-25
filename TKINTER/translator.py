from googletrans import Translator
from tkinter import *

# List of available languages
choose_languages = (
    'Afrikaans', 'Albanian', 'Arabic', 'Armenian', 'Azerbaijani', 'Basque', 'Belarusian',
    'Bengali', 'Bosnian', 'Bulgarian', 'Catalan', 'Cebuano', 'Chichewa', 'Chinese', 'Corsican'
    # Add the remaining languages here
)

# Translator function
def translate_text():
    source_language = source_var.get()
    destination_language = destination_var.get()
    text_to_translate = entry_text.get()

    translator = Translator()

    try:
        translated_text = translator.translate(text_to_translate, src=source_language, dest=destination_language).text
        result_text.set(f"Translated Text: {translated_text}")
    except Exception as e:
        result_text.set(f"Error: {e}")

# Clear function
def clear_fields():
    entry_text.delete(0, END)
    result_text.set("")

# Create GUI
root = Tk()
root.title("Language Translator")

# Source Language Dropdown
source_var = StringVar(root)
source_var.set(choose_languages[0])  # Set the default source language
source_label = Label(root, text="Select Source Language:")
source_label.grid(row=0, column=0, padx=10, pady=10)
source_dropdown = OptionMenu(root, source_var, *choose_languages)
source_dropdown.grid(row=0, column=1, padx=10, pady=10)

# Destination Language Dropdown
destination_var = StringVar(root)
destination_var.set(choose_languages[1])  # Set the default destination language
destination_label = Label(root, text="Select Destination Language:")
destination_label.grid(row=1, column=0, padx=10, pady=10)
destination_dropdown = OptionMenu(root, destination_var, *choose_languages)
destination_dropdown.grid(row=1, column=1, padx=10, pady=10)

# Text Entry
entry_label = Label(root, text="Enter Text to Translate:")
entry_label.grid(row=2, column=0, padx=10, pady=10)
entry_text = Entry(root, width=40)
entry_text.grid(row=2, column=1, padx=10, pady=10)

# Translate Button
translate_button = Button(root, text="Translate", command=translate_text)
translate_button.grid(row=3, column=0, pady=10)

# Clear Button
clear_button = Button(root, text="Clear", command=clear_fields)
clear_button.grid(row=3, column=1, pady=10)

# Result Label
result_text = StringVar()
result_label = Label(root, textvariable=result_text, wraplength=400)
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
