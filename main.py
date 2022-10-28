#---------------------------------------------------------------------------------
#
# Work Timer Program:
# 
# Version: 2.0
#
#------------------------------------------------------------------------------

from tkinter import *
from turtle import width
import math

# ---------------------------- CONSTANTS ------------------------------- #
# Initializes variables for project colors, timer, main font, and number
# of reps

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

# Resets the window timer # 

def reset_timer():
  window.after_cancel(timer) # make a call to cancel the timer within the window
  
  # resets window specific variables: like timer variables and labels 
  canvas.itemconfig(timer_text, text="00:00") # Note this is a canvas not a label :)
  head_label.config(text = "Timer")
  check_marks.config(text="")
  # Note: Unlike C#, Java or C++, you still need to use the global keywork prior to using an
  # already define global variable.  Trust me, python will produce an error if you do not.
  global reps 
  reps = 0

# TIMER MECHANISM #
# Starts and restarts the clock.  Also changes head label to correct state (i.e. work or break) 
def start_timer():
  
  global reps # As stated in earlier comment
  
  reps += 1
  # Time variables
  work_sec = WORK_MIN * 60
  short_break_sec = SHORT_BREAK_MIN * 60
  long_break_sec = LONG_BREAK_MIN * 60
  
  # Determines if we are still on work time or a short/long break.
  if reps % 8 == 0:
    count_down(long_break_sec)
    head_label.config(text="Break",fg=RED)
  elif reps % 2 == 0:
    count_down(short_break_sec)
    head_label.config(text="Break",fg=PINK)
  else:
    count_down(work_sec)
    head_label.config(text="Work", fg=GREEN)
   

# COUNTDOWN #
# Counts down the seconds to zero 

def count_down(count):
  
  count_min = math.floor(count / 60) # do want a float number here
  count_sec = count % 60
  
  # Makes sure the output to the user looks like an actual clock
  if count_sec < 0:
    count_sec = "00"
  
  if count_sec <= 9:
    count_sec = f"0{count_sec}"  
  
  # change the text on the canvas.
  canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
  
  # If time is still greater than zero, keep counting.
  # Else change state and increment the checkmark count
  if count > 0:
    global timer
    timer = window.after(1000, count_down, count - 1)
  else:
    start_timer()
    # Local variables
    marks = ""
    work_session = math.floor(reps/2)
    for _ in range(work_session):
      marks += "✓"
    # update check_marks label  
    check_marks.config(text=marks)
      
    
# User Interface #
# Setting up the window and all the graphics

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

# Header Label
head_label = Label(text="Timer", font=(FONT_NAME, 30, "bold"), bg=YELLOW, fg=GREEN)
head_label.grid(column=1, row=0)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 50))

canvas.grid(column=1, row=1)

# Buttons
start_btn = Button(text="Start", command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", command=reset_timer)
reset_btn.grid(column=2, row=2)

# check_mark label
check_marks = Label(font=(FONT_NAME, 12, "bold"), fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

# Loop main window
window.mainloop()
