import tkinter
from tkinter import PhotoImage
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checkmark = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text,  text="00:00")
    checkmark_label.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break)
        timer_label.config(text="LongBreak", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break)
        timer_label.config(text="ShortBreak", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count -1)
    else:
        start_timer()
        if reps % 2 == 0:
            global checkmark
            checkmark += "√"
            checkmark_label.config(text=checkmark)
# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Timer label
timer_label = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 45))
timer_label.grid(column=1, row=0)

# Tomato canvas
canvas = tkinter.Canvas(width=200 , height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
# Clock in tomato
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
# canvas.pack()
canvas.grid(column=1, row=1)

# Start button
start_button = tkinter.Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

# reset button
reset_button = tkinter.Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

# Checkmark label , text = "✓"
checkmark_label = tkinter.Label(text=checkmark, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35))
checkmark_label.grid(column=1, row=3)

window.mainloop()