from tkinter import *
import time

root = Tk()
root.title("Click Counter")
root.columnconfigure(0, weight=1)
count = 0
time_var = 10.00
flag = False


def countdown():
    global time_var
    global flag
    if time_var == 0 or time_var < 0:
        flag = False
    if flag:
        time_var -= 0.1
        timer.configure(text=f"Your time left is: {time_var}")
    root.after(100, countdown)


def increase():
    global count
    global flag
    global time_var
    if not flag:
        flag = True
        countdown()
    if time_var > 0:
        count += 1
        counter.configure(text=f"Your count is: {count}")


counter = Label(text=f"Your count is: {count}")
counter.grid()
timer = Label(text=f"Your time left is: {time_var}")
timer.grid()
button = Button(text="Click to increase", command=increase)
button.grid()


root.mainloop()
