import tkinter as tk

def create_cartoon(canvas):
    # Draw the face
    face = canvas.create_oval(50, 50, 250, 250, fill="skyblue")

    # Draw the triangular ears
    left_ear = canvas.create_polygon(50, 50, 30, 100, 70, 100, fill="skyblue")
    right_ear = canvas.create_polygon(250, 50, 230, 100, 270, 100, fill="skyblue")

    # Draw the eyes
    left_eye = canvas.create_oval(100, 100, 130, 130, fill="white")
    right_eye = canvas.create_oval(170, 100, 200, 130, fill="white")

    # Draw the pupils
    left_pupil = canvas.create_oval(115, 115, 125, 125 ,fill="black")
    right_pupil = canvas.create_oval(185 ,115 ,195 ,125 ,fill="black")

    # Draw the mouth
    mouth = canvas.create_arc(120 ,150 ,180 ,190,start=0,
                             extent=-180,
                             style=tk.ARC)

    # Draw the oval legs
    left_leg = canvas.create_oval(110, 250, 130, 300, fill="skyblue")
    right_leg = canvas.create_oval(170, 250, 190, 300, fill="skyblue")

# Create a window
root = tk.Tk()
root.title("Cartoon Drawing with Tkinter")

# Create a drawing canvas
canvas = tk.Canvas(root,width=300,height=350,bg='black')
canvas.pack()

create_cartoon(canvas)

# Run the Tkinter event loop
root.mainloop()
