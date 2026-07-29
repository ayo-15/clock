import tkinter as tk
from time import strftime
def update_time():
    current_time = strftime('%H:%M:%S')
    label.config(text=current_time)
    label.after(1000, update_time)
root = tk.Tk()
root.title("Digital Clock")
root.geometry("300x100")
label = tk.Label(
    root,
    font=("Arial", 40, "bold"),
    background="light blue",
    foreground="white"
)
label.pack(anchor="center")
update_time()
root.mainloop()