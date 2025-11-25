import tkinter as tk
import time

def countdown(time_sec):
    while time_sec > -1:
        mins, secs = divmod(time_sec, 60) 
        time_label.config(text=f"{mins:02}:{secs:02}")
        root.update()
        time.sleep(1)
        time_sec -= 1
    time_label.config(text="Time's Up!")

def start_countdown():
    try:
        time_sec = int(entry.get())
        countdown(time_sec)
    except ValueError:
        time_label.config(text="Invalid Input")

root = tk.Tk()
root.title("Countdown Timer")

time_label = tk.Label(root, font=("Arial", 48))
time_label.pack()

entry = tk.Entry(root)
entry.pack()

start_button = tk.Button(root, text="Start", command=start_countdown)
start_button.pack()

root.mainloop()