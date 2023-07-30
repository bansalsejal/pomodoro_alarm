import math
import time
from tkinter import *

YELLOW = "#FEFF86"
SKY = "#B0DAFF"
OCEAN_BLUE = "#19A7CE"
BLUE = "#146C94"
WORK_MIN = 25
SHORT_BREAK = 5
LONG_BREAK = 20
REPS = 0
timer= NONE

def timer_reset():
    global REPS, timer
    window.after_cancel(timer)
    REPS=0
    canvas.itemconfig(canvas_text, text="00 00")
    my_label.config(text="TIMER")


def timer_start():
    global REPS
    REPS += 1
    if REPS == 9:
        timer_reset()
    elif REPS % 2 != 0:
        my_label.config(text="WORK")
        timer_countdown(WORK_MIN * 60)
    elif REPS % 8 == 0:
        my_label.config(text="LONG BREAK")
        timer_countdown(LONG_BREAK * 60)
    else:
        my_label.config(text="SHORT BREAK")
        timer_countdown(SHORT_BREAK * 60)


def timer_countdown(count):
    global REPS
    min_count = math.floor(count / 60)
    sec_count = count % 60
    if min_count < 10:
        min_count = f"0{min_count}"
    if sec_count ==0:
        sec_count = f"0{sec_count}"
    canvas.itemconfig(canvas_text, text=f"{min_count} {sec_count}")
    if count > 0:
        global timer
        timer = window.after(1000, timer_countdown, count-1)
    else:
        timer_start()
        mark = "✓" * math.floor(REPS/2)
        check.config(text=mark)


window = Tk()
window.config(bg=SKY, pady=30, padx=30)

my_label = Label(text="TIMER", font=("ARIAL", 30, "bold"), fg=BLUE, bg=SKY)
my_label.grid(row=0, column=1)

canvas = Canvas(window, width=180, height=194, bg=SKY, highlightthickness=0)
bg_image = PhotoImage(file="alarm_image.png")
canvas.create_image(90, 97, image=bg_image)
canvas_text = canvas.create_text(90, 105, text="00 00", font=("Arial", 20, "bold"), fill=BLUE)
canvas.grid(row=1, column=1, pady=10)

start_btn = Button(text="START", bg=SKY, fg=BLUE, command=timer_start)
start_btn.grid(row=2, column=0)

reset_btn = Button(text="RESET", bg=SKY, fg=BLUE, command=timer_reset)
reset_btn.grid(row=2, column=2)

check = Label(bg=SKY, fg=BLUE)
check.grid(row=3, column=1)

window.mainloop()
