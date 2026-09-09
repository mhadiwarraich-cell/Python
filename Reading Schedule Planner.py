from tkinter import *

def open_planner():
    planner = Toplevel(window)
    planner.title("Reading Schedule Planner")
    planner.geometry("400x300")

    Label(planner, text="Total Pages").grid(row=0, column=0, padx=10, pady=10)
    pages = Entry(planner)
    pages.grid(row=0, column=1)

    Label(planner, text="Pages Per Day").grid(row=1, column=0, padx=10, pady=10)
    daily = Entry(planner)
    daily.grid(row=1, column=1)

    result = Label(planner, text="")
    result.grid(row=3, column=0, columnspan=2, pady=20)

    def calculate():
        try:
            total = int(pages.get())
            per_day = int(daily.get())

            days = total // per_day
            remaining = total % per_day

            result.config(text="Complete Days: " + str(days) +
                          "\nRemaining Pages: " + str(remaining))
        except:
            result.config(text="Please enter valid numbers!")

    Button(planner, text="Calculate", command=calculate).grid(
        row=2, column=0, columnspan=2, pady=10)

window = Tk()
window.title("Reading Schedule Planner")
window.geometry("400x200")

Label(window, text="Reading Schedule Planner").pack(pady=30)
Button(window, text="Open Planner", command=open_planner).pack()

window.mainloop()