import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser


class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Paint App")

        self.pen_mode = tk.StringVar()
        self.pen_mode.set("pen")

        self.color = "black"
        self.brush_size = 2

        self.canvas = tk.Canvas(root, bg="white", width=800, height=600)
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        self.pen_button = ttk.Radiobutton(root, text="Pen", variable=self.pen_mode, value="pen")
        self.brush_button = ttk.Radiobutton(root, text="Brush", variable=self.pen_mode, value="brush")
        self.color_button = ttk.Button(root, text="Color", command=self.choose_color)
        self.eraser_button = ttk.Button(root, text="Eraser", command=self.set_eraser)
        self.size_label = ttk.Label(root, text="Size:")
        self.size_scale = ttk.Scale(root, from_=1, to=20, orient=tk.HORIZONTAL, length=100, command=self.set_size)

        self.pen_button.pack(side=tk.LEFT, padx=5)
        self.brush_button.pack(side=tk.LEFT, padx=5)
        self.color_button.pack(side=tk.LEFT, padx=5)
        self.eraser_button.pack(side=tk.LEFT, padx=5)
        self.size_label.pack(side=tk.LEFT, padx=5)
        self.size_scale.pack(side=tk.LEFT, padx=5)

        self.canvas.bind("<B1-Motion>", self.paint)

    def choose_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.color = color

    def set_eraser(self):
        self.pen_mode.set("eraser")

    def set_size(self, val):
        self.brush_size = int(val)

    def paint(self, event):
        x1, y1 = (event.x - self.brush_size), (event.y - self.brush_size)
        x2, y2 = (event.x + self.brush_size), (event.y + self.brush_size)

        if self.pen_mode.get() == "pen":
            self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline=self.color)
        elif self.pen_mode.get() == "brush":
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.color, outline=self.color)
        elif self.pen_mode.get() == "eraser":
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="white")


if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()
