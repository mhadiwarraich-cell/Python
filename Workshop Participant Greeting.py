import tkinter as tk

def check_in():
    name = name_entry.get()
    message.delete("1.0", tk.END)
    message.insert(tk.END, "Welcome " + name + "!\n")
    message.insert(tk.END, "Workshop Date: 1 September 2026")

window = tk.Tk()
window.title("Workshop Participant Greeting")
window.geometry("400x300")

tk.Label(window, text="Workshop Participant Greeting").pack()
tk.Label(window, text="Enter your name:").pack()

name_entry = tk.Entry(window)
name_entry.pack()

tk.Button(window, text="Check In", command=check_in).pack()

message = tk.Text(window, height=5, width=40)
message.pack()

window.mainloop()