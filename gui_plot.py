from tkinter import *
from tkinter import ttk
import matplotlib

# Notes
# The button type that will be used for word mode and character mode is called radio button I think
root = Tk()
frm = ttk.Frame(padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=1)
root.mainloop()