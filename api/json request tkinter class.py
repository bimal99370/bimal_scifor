import requests
import json
import tkinter as tk


# class Link:
#     def display(self):
#         # Update Label widgets with extracted data
#         for key, label in self.labels.items():
#             value = self.data.get(key, "N/A")
#             label.config(text=f"{key.capitalize()}: {value}")
#

class Link:
    def display(self):
        # Extract specific data from the JSON
        id = self.data.get("_id", "N/A")
        tags = self.data.get("tags", "N/A")
        slug = self.data.get("authorSlug", "N/A")
        length = self.data.get("length", "N/A")
        date_modified = self.data.get("dateAdded", "N/A")
        date_added = self.data.get("dateModified", "N/A")
        content = self.data.get("content", "N/A")
        author = self.data.get("author", "N/A")

        # Clear previous content
        self.display_text.delete(1.0, tk.END)

        # Insert formatted text using tags
        self.display_text.insert(tk.END, f"ID: {id}\n", "blue")
        self.display_text.insert(tk.END, f"Tags: {tags}\n", "green")
        self.display_text.insert(tk.END, f"Slug: {slug}\n", "red")
        self.display_text.insert(tk.END, f"Length: {length}\n", "purple")
        self.display_text.insert(tk.END, f"Date Modified: {date_modified}\n", "brown")
        self.display_text.insert(tk.END, f"Date Added: {date_added}\n", "orange")
        self.display_text.insert(tk.END, f"Content: {content}\n", "black")
        self.display_text.insert(tk.END, f"Author: {author}\n", "darkblue")

    def __init__(self):
        self.url = "https://api.quotable.io/random"
        self.response = requests.get(self.url)
        self.data = self.response.json()

        self.window = tk.Tk()
        self.window.geometry("500x600")
        self.window.resizable(True, False)
        self.window.configure(bg="lightblue")

        # Create a Text widget
        self.display_text = tk.Text(self.window, width=100, height=20, wrap=tk.WORD)
        self.display_text.pack(pady=20)

        # Configure tags for different colors
        self.display_text.tag_configure("blue", foreground="blue", font=("Helvetica", 10, "bold"))
        self.display_text.tag_configure("green", foreground="green", font=("Helvetica", 10, "bold"))
        self.display_text.tag_configure("red", foreground="red", font=("Helvetica", 10, "bold"))
        self.display_text.tag_configure("purple", foreground="purple", font=("Helvetica", 10, "bold"))
        self.display_text.tag_configure("brown", foreground="brown", font=("Helvetica", 10, "bold"))
        self.display_text.tag_configure("orange", foreground="orange", font=("Helvetica", 10, "bold"))
        self.display_text.tag_configure("black", foreground="black", font=("Helvetica", 10, "bold"))
        self.display_text.tag_configure("darkblue", foreground="darkblue", font=("Helvetica", 10, "bold"))

        # Create a Button to fetch and display JSON data
        self.button = tk.Button(self.window, text="Click here", command=self.display)
        self.button.pack(pady=20)

if __name__ == "__main__":
    link_instance = Link()
    link_instance.window.mainloop()



# import requests
# import json
# import tkinter as tk
#
# class Link:
#     def display(self):
#         # Extract specific data from the JSON
#         id = self.data.get("_id", "N/A")
#         tags = self.data.get("tags", "N/A")
#         slug = self.data.get("authorSlug", "N/A")
#         length = self.data.get("length", "N/A")
#         date_modified = self.data.get("dateAdded", "N/A")
#         date_added = self.data.get("dateModified", "N/A")
#         content = self.data.get("content", "N/A")
#         author = self.data.get("author", "N/A")
#
#         # Update Label widgets with extracted data
#         self.id_label.config(text=f"ID: {id}")
#         self.tags_label.config(text=f"Tags: {tags}")
#         self.slug_label.config(text=f"Slug: {slug}")
#         self.length_label.config(text=f"Length: {length}")
#         self.date_modified_label.config(text=f"Date Modified: {date_modified}")
#         self.date_added_label.config(text=f"Date Added: {date_added}")
#         self.content_label.config(text=f"Content: {content}")
#         self.author_label.config(text=f"Author: {author}")
#
#     def __init__(self):
#         self.url = "https://api.quotable.io/random"
#         self.response = requests.get(self.url)
#         self.data = self.response.json()
#
#         self.window = tk.Tk()
#         self.window.geometry("500x600")
#         self.window.resizable(True, False)
#         self.window.configure(bg="lightblue")
#
#         # Create Label widgets for each key-value pair
#         self.id_label = tk.Label(self.window, font=("Helvetica", 10, "bold"))
#         self.tags_label = tk.Label(self.window, font=("Helvetica", 10, "bold"))
#         self.slug_label = tk.Label(self.window, font=("Helvetica", 10, "bold"))
#         self.length_label = tk.Label(self.window, font=("Helvetica", 10, "bold"))
#         self.date_modified_label = tk.Label(self.window, font=("Helvetica", 10, "bold"))
#         self.date_added_label = tk.Label(self.window, font=("Helvetica", 10, "bold"))
#         self.content_label = tk.Label(self.window, font=("Helvetica", 10, "bold"))
#         self.author_label = tk.Label(self.window, font=("Helvetica", 10, "bold"))
#
#         # Create a Button to fetch and display JSON data
#         self.button = tk.Button(self.window, text="Click here", command=self.display)
#         self.button.pack(pady=20)
#
#         # Pack Label widgets
#         self.id_label.pack()
#         self.tags_label.pack()
#         self.slug_label.pack()
#         self.length_label.pack()
#         self.date_modified_label.pack()
#         self.date_added_label.pack()
#         self.content_label.pack()
#         self.author_label.pack()
#
# if __name__ == "__main__":
#     link_instance = Link()
#     link_instance.window.mainloop()
#
