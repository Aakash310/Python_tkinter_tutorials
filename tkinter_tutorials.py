#starte code
import tkinter as tk
from tkinter import ttk
from csv import DictWriter
import os
win = tk.Tk()

#title of window
win.title('GUI')

#create label
name_label=ttk.Label(win,text="Enter your name:")
name_label.grid(row=0,column=0,sticky=tk.W)

email_label=ttk.Label(win,text="Enter your email:")
email_label.grid(row=1,column=0,sticky=tk.W)

age_label=ttk.Label(win,text="Enter your age:")
age_label.grid(row=2,column=0,sticky=tk.W)

gender_label=ttk.Label(win,text="Enter your gender:")
gender_label.grid(row=3,column=0,sticky=tk.W)

name_var=tk.StringVar()
name_entrybox=ttk.Entry(win,width=16,textvariable=name_var)
name_entrybox.grid(row=0,column=1)

email_var=tk.StringVar()
email_entrybox=ttk.Entry(win,width=16,textvariable=email_var)
email_entrybox.grid(row=1,column=1)

age_var=tk.StringVar()
age_entrybox=ttk.Entry(win,width=16,textvariable=age_var)
age_entrybox.grid(row=2,column=1)

#Create ComboBox
gender_var=tk.StringVar()
gender__combobox=ttk.Combobox(win,width=14,textvariable=gender_var,state='readonly')
gender__combobox['values']=('Male','Female','Others')
gender__combobox.current(0)
gender__combobox.grid(row=3,column=1)

#Radio Button
usertype=tk.StringVar()

radiobtn1=ttk.Radiobutton(win,text='Student',value='Student',variable=usertype)
radiobtn1.grid(row=4,column=0)

radiobtn2=ttk.Radiobutton(win,text='Teacher',value='Teacher',variable=usertype)
radiobtn2.grid(row=4,column=1)

#Check Button
check_var = tk.IntVar()
checkbtn=ttk.Checkbutton(win,text="check if you want to subscribe to our newsletter",variable=check_var)
checkbtn.grid(row=5,columnspan=3)

#create Button
# def action():
#     username = name_var.get()
#     userage = age_var.get()
#     user_email = email_var.get()
#     print(f'{username}is {userage} years old and his EmailId is {user_email}')
#     user_gender = gender_var.get()
#     user_type = usertype.get()
#     if check_var.get() == 0:
#         subscribed = 'NO'
#     else:
#         subscribed='YES'
#     print(user_gender,user_type,subscribed)    

#     with open('file.txt','a') as f:
#         f.write(f'{username},{user_email},{userage},{user_gender},{user_type},{subscribed}\n')   
#     name_entrybox.delete(0,tk.END)     
#     email_entrybox.delete(0,tk.END)  
#     age_entrybox.delete(0,tk.END)  
#     #name_label.configure(foreground='blue')
    
def action():
    username = name_var.get()
    userage = age_var.get()
    user_email = email_var.get()
    print(f'{username}is {userage} years old and his EmailId is {user_email}')
    user_gender = gender_var.get()
    user_type = usertype.get()
    if check_var.get() == 0:
        subscribed = 'NO'
    else:
        subscribed='YES'

    #write to csv file
    with open('file.csv','a',newline='') as f:
        dict_writer = DictWriter(f,fieldnames=['UserName','User Email Address','User Age','User Gender',
        'User Type','Subscribed'])
        if os.stat('file.csv').st_size==0:
            dict_writer.writeheader()
        dict_writer.writerow({
            'UserName':username,
            'User Email Address' : user_email,
            'User Age' : user_email,
            'User Gender' : user_gender,
            'User Type' : user_type,
            'Subscribed' : subscribed
        })

    name_entrybox.delete(0,tk.END)     
    email_entrybox.delete(0,tk.END)  
    age_entrybox.delete(0,tk.END)  
    #name_label.configure(foreground='blue')    


submit_button=ttk.Button(win,text="Submit", command=action)
submit_button.grid(row=6,column=0)

win.mainloop()