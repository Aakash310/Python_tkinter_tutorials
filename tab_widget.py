import tkinter as tk
from tkinter import ttk
win=tk.Tk()
win.title('TAB CONTROL')

nb =ttk.Notebook(win)
page1 = ttk.Frame(nb)
page2 = ttk.Frame(nb)
nb.add(page1,text='ONE')
nb.add(page2,text='TWO')
#nb.grid(row=0,column=0)
nb.pack(expand=True,fill='both')

label1 = ttk.Label(page1,text="This is label :")
label1.grid(row=0,column=0)

entry1 = ttk.Entry(page1,width=16)
entry1.grid(row=0,column=1)

win.mainloop()