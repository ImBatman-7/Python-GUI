import tkinter as tk
from tkinter import ttk
import os
from csv import DictWriter

win = tk.Tk()
win.title('GUI')


#create lables
name_label = ttk.Label(win, text='Enter your name: ')
name_label.grid(row=0, column=0, sticky=tk.W)


email_label = ttk.Label(win, text='Enter your email: ')
email_label.grid(row=1, column=0, sticky=tk.W)


age_label = ttk.Label(win, text='Enter your age: ')
age_label.grid(row=2, column=0, sticky=tk.W)


gender_label = ttk.Label(win, text='select your gender: ')
gender_label.grid(row=3, column=0, sticky=tk.W)

#create entry Box
name_var = tk.StringVar()
name_entrybox = ttk.Entry(win, width = 16, textvariable= name_var)
name_entrybox.grid(row=0, column=1)
name_entrybox.focus()

email_var = tk.StringVar()
email_entrybox = ttk.Entry(win, width = 16, textvariable= email_var)
email_entrybox.grid(row=1, column=1)

age_var = tk.StringVar()
age_entrybox = ttk.Entry(win, width = 16, textvariable= age_var)
age_entrybox.grid(row=2, column=1)

gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(win, width = 13, textvariable= gender_var, state='readonly')
gender_combobox['values']= ('Male', "Female", "Other")
gender_combobox.grid(row=3, column=1)
gender_combobox.current(0)
 
#create radio button

typesofuser = tk.StringVar()
r1 = ttk.Radiobutton(win, text='student', value='student', variable=typesofuser)
r1.grid(row=4, column=0)

r2 = ttk.Radiobutton(win, text='teacher', value='teacher', variable=typesofuser)
r2.grid(row=4, column=1)

#create check button
checkbtn_var = tk.IntVar()
checkbtn = ttk.Checkbutton(win, text='check if you want to get the latest updates', variable=checkbtn_var)
checkbtn.grid(row=5, columnspan=3)

#create button

# def action():
#   username = name_var.get()
#   userage = age_var.get()
#   useremail = email_var.get()
#   usergender = gender_var.get()
#   usertype = typesofuser.get()
#   usercheck = checkbtn_var.get()

#   print(f'{username} is of {userage} years,\n email is {useremail}, \n gender is{usergender}, \n type is {usertype}, \n checked value is {usercheck}')

#   with open('tkintergui.txt', 'a')as f:
#     f.write(f'{username} is of {userage} years,\n email is {useremail}, \n gender is{usergender}, \n type is {usertype}, \n checked value is {usercheck}\n') 

#   name_entrybox.delete(0, tk.END)
#   age_entrybox.delete(0, tk.END)
#   email_entrybox.delete(0, tk.END)
#   name_label.configure(foreground='blue')

#write to csv File

def action():
  username = name_var.get()
  userage = age_var.get()
  useremail = email_var.get()
  usergender = gender_var.get()
  usertype = typesofuser.get()
  usercheck = checkbtn_var.get()

  with open('fileeee.csv', 'a', newline='')as f:
    dict_writer = DictWriter(f, fieldnames = ['User name', 'user email address', 'user age', 'user gender', 'user type', 'subbed'])
    if os.stat('fileeee.csv').st_size==0:
        dict_writer.writeheader()

    dict_writer.writerow({
        'User name': username,
        'user email address' : userage,
        'user age' : useremail,
        'user gender' : usergender,
        'user type' : usertype,
        'subbed' : usercheck

        })

    name_entrybox.delete(0, tk.END)
    age_entrybox.delete(0, tk.END)
    email_entrybox.delete(0, tk.END)
    name_label.configure(foreground='blue')


submit_button = ttk.Button(win, text='Submit', command=action)
submit_button.grid(row=6, column=2, sticky=tk.W)

win.mainloop()


