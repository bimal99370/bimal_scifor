import tkinter as tk
from PIL import Image, ImageTk



# Create the main window
root = tk.Tk()
root.title("Endangered Animals")


# Create a label for the heading
heading_label = tk.Label(root, text="Animal Kingdom", font=("Arial", 28, "bold"))
heading_label.grid(row=0, column=0, columnspan=3)

# Get the window size
window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()

# Load the background image
background_image = Image.open("jungle_background.jpg")

# Resize the background image to match the window size
background_image = background_image.resize((window_width, window_height))

# Convert the background image to PhotoImage
background_photo = ImageTk.PhotoImage(background_image)

# Create a label to display the background image
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0)  # Use relwidth and relheight to fill the whole page


# Load images
bengal_tiger_image = Image.open("bengal_tiger.jpg")
asiatic_lion_image = Image.open("asiatic_lion.jpg")
snow_leopard_image = Image.open("snow_leopard.jpg")
black_buck_image = Image.open("black_buck.jpg")

# Convert images to PhotoImage
bengal_tiger_photo = ImageTk.PhotoImage(bengal_tiger_image)
asiatic_lion_photo = ImageTk.PhotoImage(asiatic_lion_image)
snow_leopard_photo = ImageTk.PhotoImage(snow_leopard_image)
black_buck_photo = ImageTk.PhotoImage(black_buck_image)

# Create labels for animal names and images
animals_info = [
    ("Bengal Tiger", bengal_tiger_photo, "The Bengal Tiger is the national animal of both India and Bangladesh..."),
    ("Asiatic Lion", asiatic_lion_photo, "The Asiatic Lion also known as Persian Lion..."),
    ("Snow Leopard", snow_leopard_photo, "The snow leopard is a large cat native to the mountain ranges..."),
    ("Black Buck", black_buck_photo, "The Blackbuck is an antelope species native to the Indian subcontinent...")
]






# Create labels for animal names and images
for i in range(len(animals_info)):
    name, photo, info = animals_info[i]

    # Animal name label
    name_label = tk.Label(root, text=name,background="lightgreen",font="bold")
    name_label.grid(row=i+1, column=3)

    # Animal image label
    image_label = tk.Label(root, image=photo)
    image_label.grid(row=i+1, column=4)

    # Animal info label with word wrap
    info_label = tk.Label(root, text=info,background="darkgreen",foreground="white",font="bold", width=50, height=6,
                          wraplength=250,
                          justify="right")
    info_label.grid(row=i+1, column=5)






# ---------------------------  another for loop ---------------------------------------







# for i in range(len(animals_info)):
#     name, photo, info = animals_info[i]
#
#     # Animal name label
#     name_label = tk.Label(root, text=name)
#     name_label.grid(row=i//2, column=2*(i%2))
#
#     # Animal image label
#     image_label = tk.Label(root, image=photo)
#     image_label.grid(row=i//2, column=2*(i%2)+1)
#
#     # Animal info label with word wrap
#     info_label = tk.Label(root, text=info, width=50, height=6,
#                           wraplength=250,
#                           justify="left")
#     info_label.grid(row=i//2, column=2*(i%2)+2)
#


# Run the application loop
root.mainloop()
