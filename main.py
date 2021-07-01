from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfilename

edit_command_list = ["Undo", "Redo", "Cut", "Copy", "Paste", "Select All", "Search", "Delete"]

filename = ''


def new_file():
    global filename
    save_old_file()
    text_space.delete('1.0', 'end')
    filename = ''


def open_file():
    global filename
    filename = askopenfilename(mode='r+')
    if filename is not None:
        t = filename.read()
        text_space.delete("0.0", "end")
        text_space.insert("0.0", t)
        text_space.focus()


def save_old_file():
    global filename
    if filename == '':
        filename = asksaveasfile(mode='w')
    if filename is not None:
        data = text_space.get('1.0', 'end')
        filename.write(data)


def save():
    global filename
    files = [('All Files', '*.*'),
             ('Text Document', '*.txt')]
    filename = asksaveasfile(filetypes=files, defaultextension=files, mode='w')
    save_old_file()


def clear():
    save()
    text_space.delete("0.0", "end")


root = Tk()
root.minsize(height=400, width=400)
root.title("WritePad")

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

text_space = Text(root, yscrollcommand=scrollbar.set, undo=True)
text_space.pack(expand=True, fill=BOTH)

scrollbar.config(command=text_space.yview)

menu_bar = Menu(root)
file_option_menu = Menu(menu_bar, tearoff=0)
file_option_menu.add_command(label="New", command=new_file)
file_option_menu.add_command(label="Open", command=open_file)
file_option_menu.add_command(label="Save", command=save_old_file)
file_option_menu.add_command(label="Save As...", command=save)
file_option_menu.add_command(label="Close", command=clear)

file_option_menu.add_separator()
file_option_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_option_menu)

edit_option_menu = Menu(menu_bar, tearoff=0)
for command in edit_command_list:
    edit_option_menu.add_command(label=command)
menu_bar.add_cascade(label="Edit", menu=edit_option_menu)

help_option_menu = Menu(menu_bar, tearoff=0)
help_option_menu.add_command(label="About")
menu_bar.add_cascade(label="Help", menu=help_option_menu)

root.config(menu=menu_bar)
root.mainloop()
