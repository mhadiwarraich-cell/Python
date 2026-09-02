from tkinter import *

def setup():
    name = name_entry.get()
    pin = pin_entry.get()

    output.delete("1.0", END)
    output.insert(END, "Account: " + name + "\n")
    output.insert(END, "PIN: " + "*" * len(pin))

window = Tk()
window.title("ATM PIN Setup")
window.geometry("400x400")

Label(window, text="Account Name").place(x=30, y=30)
name_entry = Entry(window)
name_entry.place(x=130, y=30)

Label(window, text="PIN").place(x=30, y=70)
pin_entry = Entry(window, show="*")
pin_entry.place(x=130, y=70)

Button(window, text="Set PIN", command=setup).place(x=160, y=110)

output = Text(window, width=40, height=5)
output.place(x=30, y=160)

window.mainloop()