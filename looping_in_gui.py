import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title('LOOP')

labels = ['name : ', 'age : ', 'city : ']


for i in range(len(labels)):
    cur_label = ttk.Label(win, text=labels[i])
    cur_label.grid(row=i, column=0, sticky=tk.W, padx=4, pady=2)


name_var = tk.StringVar()


user_info = {
    'name' : tk.StringVar(),
    'age' : tk.StringVar(),
    'city' : tk.StringVar() 
}

counter=0
for i in user_info:
    entrybox = 'entry' + i
    entrybox = ttk.Entry(win, width=16, textvariable=user_info[i])
    entrybox.grid(row=counter, column=1, padx=4, pady=2)
    counter +=1


def action():
    print('yes')    


sub_btn=ttk.Button(win, text='Submit', command=action)
sub_btn.grid(row=3, column=0)

win.mainloop()    