from tkinter import *
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
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer")
    check_marks.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps % 2 == 1:
        label.config(text="WORK", fg=GREEN)
        count_down(work_sec)

    elif reps == 8:
        label.config(text="BREAK", fg=RED)
        count_down(long_break_sec)

    else:
        label.config(text="BREAK", fg=PINK)
        count_down(short_break_sec)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    global reps
    global timer
    count_min = math.floor(count/60)
    count_sec = count % 60
    min_text = count_min
    sec_text = count_sec
    if count_min < 10:
        min_text = f"0{count_min}"
    if count_sec < 10:
        sec_text = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{min_text}:{sec_text}")

    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)

        for _ in range(work_session):
            marks += tick
        check_marks.config(text=marks)




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112,image=tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)


label = Label(text="Timer", font=(FONT_NAME, 30, 'bold'), fg=GREEN, highlightthickness=0)
label.config(bg=YELLOW)
label.grid(column=1, row=0)



tick = "✔"
start_button = Button(text="Start", command=start_timer, relief=GROOVE, bg="white", bd=0, highlightthickness=0)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", command=reset_timer, relief=GROOVE, bg="white", bd=0, highlightthickness=0)
reset_button.grid(column=2, row=2)


check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)





window.mainloop()
