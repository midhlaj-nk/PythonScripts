import tkinter as tk
from tkinter import ttk

class CustomEntry(tk.Entry):
    def __init__(self, *args, **kwargs):
        kwargs["borderwidth"] = 0
        super().__init__(*args, **kwargs)
        separator = ttk.Separator(orient="horizontal")
        separator.place(in_=self, x=0, rely=1.0, height=2, relwidth=1.0)

root = tk.Tk()
style = ttk.Style()
print(style.layout("TEntry"))
print(style.layout("TSeparator"))

for row, field in enumerate(("First", "Last")):
    label = tk.Label(root, text=field)
    entry = CustomEntry(root, width=20, highlightthickness=0)
    label.grid(row=row, column=0, sticky="e", padx=10, pady=4)
    entry.grid(row=row, column=1, sticky="ew", padx=10, pady=4)

root.mainloop()
