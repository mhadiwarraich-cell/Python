from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_letter():
    file = askopenfilename()
    if file:
        text.delete("1.0", END)
        with open(file, "r") as f:
            text.insert(END, f.read())

def save_letter():
    file = asksaveasfilename(defaultextension=".txt")
    if file:
        with open(file, "w") as f:
            f.write(text.get("1.0", END))

window = Tk()
window.title("Letter Writing Application")
window.geometry("600x400")

text = Text(window, width=60, height=15)
text.grid(row=0, column=0, columnspan=2)

Button(window, text="Open Letter", command=open_letter).grid(row=1, column=0)
Button(window, text="Save Letter", command=save_letter).grid(row=1, column=1)

window.mainloop()