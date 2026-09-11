from tkinter import *
from tkinter import ttk


# ---------------- FUNCTIONS ----------------

def place_order():
    total = 0

    for i, item in enumerate(items):
        quantity = quantities[i].get()

        if quantity.isdigit():
            total = total + int(quantity) * prices[i]

    currency = "GBP" if gbp.get() else "PKR"

    if currency == "PKR":
        total = total * 370

    result.config(text="Total Price: " + str(total) + " " + currency)


def clear_order():
    for entry in quantities:
        entry.delete(0, END)

    result.config(text="Total Price: 0 GBP")


# ---------------- MAIN WINDOW ----------------

window = Tk()
window.title("Stationery Order Management App")
window.geometry("650x550")


# ---------------- CANVAS ----------------

canvas = Canvas(window, width=650, height=550)
canvas.pack(fill="both", expand=True)

canvas.create_text(
    325, 40,
    text="Stationery Order Management App",
    font=("Arial", 22, "bold")
)

canvas.create_text(
    325, 75,
    text="Choose your stationery and enter the quantity",
    font=("Arial", 12)
)


# ---------------- STATIONERY ----------------

items = [
    "Pen",
    "Notebook",
    "Pencil",
    "Eraser",
    "Ruler",
    "Marker"
]

prices = [
    1,
    3,
    1,
    1,
    2,
    2
]

quantities = []


# ---------------- CREATE ROWS ----------------

for i, item in enumerate(items):

    ttk.Label(
        window,
        text=item
    ).place(x=150, y=120 + i * 45)

    ttk.Label(
        window,
        text="£" + str(prices[i])
    ).place(x=280, y=120 + i * 45)

    entry = ttk.Entry(
        window,
        width=10
    )

    entry.place(
        x=350,
        y=120 + i * 45
    )

    quantities.append(entry)


# ---------------- CURRENCY ----------------

gbp = BooleanVar(value=True)

ttk.Checkbutton(
    window,
    text="Use GBP",
    variable=gbp
).place(x=250, y=400)


# ---------------- BUTTONS ----------------

ttk.Button(
    window,
    text="Place Order",
    command=place_order
).place(x=220, y=440)


ttk.Button(
    window,
    text="Clear",
    command=clear_order
).place(x=340, y=440)


# ---------------- RESULT ----------------

result = ttk.Label(
    window,
    text="Total Price: 0 GBP",
    font=("Arial", 14, "bold")
)

result.place(x=240, y=490)


# ---------------- START APP ----------------

window.mainloop()