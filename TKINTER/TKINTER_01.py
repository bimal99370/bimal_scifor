import tkinter
from tkinter import *
from PIL import Image,ImageTk
win = Tk()

# win.geometry("600*400")
win.minsize(200,100)
win.maxsize(600,600)

bimal = Label(text= "BIMAL")
bimal.pack()

# photo = PhotoImage(file="aja.png")
# image = Image.open("ajay.jpg")
# photo=ImageTk.PhotoImage(image)

title_label= Label(text="bimal is a good boy",bg="red",fg = "black",padx=100,pady=90,font="comicsansms 19 bold",borderwidth=3,relief=SUNKEN)
bimal = title_label
# bimal=Label(image=photo)
bimal.pack()

# IMPORTANT PACK OPTIONS
# anchor="nw"
# side  = BOTTOM,TOP,LEFT,RIGHT
# fill
# padx
# pady
bimal.pack(side=BOTTOM,anchor="sw")

f1 = Frame(win,bg="grey",borderwidth=6,relief=SUNKEN)
f1.pack(side = LEFT)

l = Label(f1,text="projrct")
l.pack( )

#Gui logic
win.mainloop()