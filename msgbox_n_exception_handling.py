import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box
win = tk.Tk()

#label Frame
label_frame=ttk.LabelFrame(win,text="Contact Details")
label_frame.grid(row=0,column=0,padx=40,pady=10)

#labels
name_label=ttk.Label(label_frame,text="Enter your Name :")
age_label = ttk.Label(label_frame,text="Enter your Age :")

#entry box variable
name_var = tk.StringVar()
age_var = tk.StringVar()

#entry box
name_entrybox = ttk.Entry(label_frame,width=36,textvariable=name_var)
age_entrybox = ttk.Entry(label_frame,width=36,textvariable=age_var)

#grid
name_label.grid(row=0,column=0,padx=5,pady=5,sticky=tk.W)
age_label.grid(row=0,column=1,padx=5,pady=5,sticky=tk.W)
name_entrybox.grid(row=1,column=0,padx=5,pady=5,sticky=tk.W)
age_entrybox.grid(row=1,column=1,padx=5,pady=5,sticky=tk.W)

def submit():
    #m_box.showinfo('title','content of this message box!!')
    #m_box.showerror('title','content of this messgae box!!')
    #m_box.showwarning('title','content of this message box!!')
    name = name_var.get()
    age = age_var.get()
    if name =="" or age == "":
        m_box.showerror("Error","Please Fill both name and age!")
    else:
        try:
            age = int(age)
        except ValueError:
            m_box.showerror("Error","Only digits are allowed!")    
        else:
            if age<18:
                m_box.showwarning("warning","You are not 18, visit this content only at your own risk")
            print(f'{name}:{age}')        

submit_button=ttk.Button(win,text="Submit",command=submit)
submit_button.grid(row=2,columnspan=2,padx=40)
win.mainloop()