from tkinter import *
import datetime
import winsound


def set_alarm():
    set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"

    # Function to check and play the alarm sound
    def check_alarm():
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == set_alarm_time:
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
        else:
            root.after(1000, check_alarm)  # Check again after 1000ms (1 second)

    check_alarm()


# Creating the main window
root = Tk()
root.title("Alarm Clock")

# Creating and placing labels
Label(root, text="Set Alarm:", font=("Helvetica", 16)).pack(pady=10)
Label(root, text="Hour:").pack()
Label(root, text="Minute:").pack()
Label(root, text="Second:").pack()

# Creating and placing OptionMenus for hours, minutes, and seconds
hours = [str(i).zfill(2) for i in range(25)]
minutes = [str(i).zfill(2) for i in range(60)]

hour = StringVar(root)
hour.set("00")
OptionMenu(root, hour, *hours).pack()

minute = StringVar(root)
minute.set("00")
OptionMenu(root, minute, *minutes).pack()

second = StringVar(root)
second.set("00")
OptionMenu(root, second, *minutes).pack()

# Creating and placing the Start Alarm button
Button(root, text="Start Alarm", command=set_alarm).pack(pady=20)

# Running the main loop
root.mainloop()
