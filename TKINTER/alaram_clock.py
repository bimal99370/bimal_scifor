from tkinter import *
from tkinter import ttk
import datetime
import winsound


def set_alarm():
    set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"

    # Function to check and play the alarm sound
    def check_alarm():
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        current_time_label.config(text=f"Current Time: {current_time}")

        if current_time == set_alarm_time:
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
        else:
            root.after(1000, check_alarm)  # Check again after 1000ms (1 second)

    check_alarm()


# Creating the main window
root = Tk()
root.title("Alarm Clock")


root.configure(background='orange')  # Light gray color

# Styling
style = ttk.Style()
style.configure('TLabel', font=('Helvetica', 14), background='red')
style.configure('TButton', font=('Helvetica',13, "bold"), background='red', foreground='blue', padding=(10, 4))

# Creating and placing labels
ttk.Label(root, text="Set Alarm:",font=('Helvetica',15, "bold","italic"), style='TLabel').grid(row=0, column=0, columnspan=2, pady=10)
ttk.Label(root, text="Hour:", style='TLabel').grid(row=1, column=0, pady=5)
ttk.Label(root, text="Minute:", style='TLabel').grid(row=2, column=0, pady=5)
ttk.Label(root, text="Second:", style='TLabel').grid(row=3, column=0, pady=5)

# Creating and placing OptionMenus for hours, minutes, and seconds
hours = [str(i).zfill(2) for i in range(25)]
minutes = [str(i).zfill(2) for i in range(60)]

current_time = datetime.datetime.now()
current_hour = StringVar(root, value=current_time.strftime("%H"))
current_minute = StringVar(root, value=current_time.strftime("%M"))
current_second = StringVar(root, value=current_time.strftime("%S"))

hour = StringVar(root)
hour.set("00")
ttk.OptionMenu(root, hour, *hours).grid(row=1, column=1, pady=5)

minute = StringVar(root)
minute.set("00")
ttk.OptionMenu(root, minute, *minutes).grid(row=2, column=1, pady=5)

second = StringVar(root)
second.set("00")
ttk.OptionMenu(root, second, *minutes).grid(row=3, column=1, pady=5)

# Creating and placing the Start Alarm button
ttk.Button(root, text="Start Alarm", command=set_alarm, style='TButton').grid(row=4, column=0, columnspan=2, pady=20)

# Label to display current time
current_time_label = ttk.Label(root, text="Current Time: --:--:--", style='TLabel')
current_time_label.grid(row=5, column=0, columnspan=2, pady=10)

# Running the main loop
root.mainloop()
