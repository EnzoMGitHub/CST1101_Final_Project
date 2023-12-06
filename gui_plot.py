from tkinter import *
from tkinter import ttk
import matplotlib

root = Tk()
frm = ttk.Frame(padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=1)
root.mainloop()