import tkinter as tk
from PIL import Image, ImageTk

class EndangeredAnimalsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Endangered Animals Information")

        # Adjust size
        self.root.geometry("505x400")

        # Create a canvas
        self.canvas = tk.Canvas(root, width=505, height=400)
        self.canvas.pack()

        # Show image using label
        bg_image = Image.open("aja.png")
        bg_image = ImageTk.PhotoImage(bg_image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=bg_image)

        # Create a frame
        frame = tk.Frame(root)
        frame.pack()

        # Display information about endangered animals
        self.display_animal_info("Tiger", "The Bengal Tiger is the national animal of both India and Bangladesh. The tiger’s coat is yellow to light orange, with stripes ranging from dark brown to black. The number of tigers has reduced dramatically in the past few years, due to poaching and human-tiger conflict.")

        self.display_animal_info("Lion", "Asiatic Lion aka the Indian Lion or Persian Lion is a lion subspecies that is endangered. It differs from the African lion by less inflated auditory bullae, a larger tail tuft and a less developed mane.")

        self.display_animal_info("Blackbuck", "The Blackbuck is an ungulate species of antelope and it is near threatened. The main threat to this species is poaching, predation, habitat destruction, overgrazing, inbreeding and sanctuary visitors.")

        self.display_animal_info("Leopard", "The snow leopard is a large cat native to the mountain ranges in Central and South Asia. Snow leopards have long, thick fur.")

    def display_animal_info(self, name, description):
        # Create a label with the animal name
        label_name = tk.Label(self.root, text=name, font=("Helvetica", 16, "bold"))
        label_name.pack()

        # Create a label with the animal description
        label_description = tk.Label(self.root, text=description, justify=tk.LEFT)
        label_description.pack()

        # Add a separator
        separator = tk.Frame(self.root, height=2, bd=1, relief=tk.SUNKEN)
        separator.pack(fill=tk.X, padx=5, pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = EndangeredAnimalsApp(root)
    root.mainloop()
