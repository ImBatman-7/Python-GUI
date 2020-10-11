import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("MENUBAR")

#menu



def func():
    print('this is func command. ')


#SImple menubar
# menubar.add_command(label='file', command=func)
# menubar.add_command(label='edit', command=func)
# menubar.add_command(label='help', command=func)
# menubar.add_command(label='browse', command=func)

main_menu = tk.Menu(win)
file_ka_menu= tk.Menu(main_menu, tearoff=0)
file_ka_menu.add_command(label='new file', command=func)
file_ka_menu.add_separator()
file_ka_menu.add_command(label='delete file', command=func)
file_ka_menu.add_command(label='move file', command=func)


edit_ka_menu= tk.Menu(main_menu, tearoff=0)
edit_ka_menu.add_command(label='undo', command=func)
edit_ka_menu.add_command(label='redo', command=func)
edit_ka_menu.add_separator()
edit_ka_menu.add_command(label='cut', command=func)


main_menu.add_cascade(label='file', menu=file_ka_menu)
main_menu.add_cascade(label='edit', menu=edit_ka_menu)

win.config(menu=main_menu)

win.mainloop()