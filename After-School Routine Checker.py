from tkinter import *

def typed(event):
    output.config(text="Last character: " + event.char)

def clicked(event):
    output.config(text="You clicked the routine area!")

def check():
    task = entry.get()

    if task == "":
        output.config(text="⚠️ Please enter a task!")
    else:
        output.config(text="Next task: Homework")

window = Tk()
window.title("After-School Routine Checker")
window.geometry("400x300")

Label(window, text="After-School Routine").pack()

entry = Entry(window)
entry.pack()
entry.bind("<Key>", typed)

routine = Label(window, text="Click here: Routine Area", bg="lightblue")
routine.pack(pady=20)
routine.bind("<Button-1>", clicked)

Button(window, text="Check Task", command=check).pack()

output = Label(window, text="")
output.pack(pady=20)

window.mainloop()