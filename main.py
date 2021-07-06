from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfilename

edit_command_list = ["Search", "Delete"]

filename = ''

is_all_selected = False


def new_file():
    global filename
    save_old_file()
    text_space.delete('1.0', 'end')
    filename = ''


def choose_select_option():
    global is_all_selected
    if is_all_selected:
        is_all_selected = False
        text_space.tag_add("sel", '1.0', 'end')
    else:
        is_all_selected = True
        text_space.tag_remove("sel", '1.0', 'end')
    return


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


# build the frame first and get the basics handled
root = Tk()
root.minsize(height=400, width=400)
root.title("WritePad")

# set the scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# get the actual workspace for the text editor built up and set, and bind the bar to it
text_space = Text(root, yscrollcommand=scrollbar.set, undo=True)
text_space.pack(expand=True, fill=BOTH)

scrollbar.config(command=text_space.yview)

# build and set up the menu bar for all important functions
menu_bar = Menu(root)
file_option_menu = Menu(menu_bar, tearoff=0)
file_option_menu.add_command(label="New", command=new_file, accelerator="Ctrl-T")
file_option_menu.add_command(label="Open", command=open_file, accelerator="Ctrl-G")
file_option_menu.add_command(label="Save", command=save_old_file, accelerator="Ctrl-S")
file_option_menu.add_command(label="Save As...", command=save, accelerator="Ctrl-Shift-S")
file_option_menu.add_command(label="Close", command=clear, accelerator="Ctrl-B")

file_option_menu.add_separator()
file_option_menu.add_command(label="Exit", command=root.quit, accelerator="Ctrl-Q")
menu_bar.add_cascade(label="File", menu=file_option_menu)

# adding in the keyboard shortcuts
root.bind('<Control-s>', save_old_file)
root.bind('<Control-Shift-S>', save)
root.bind('<Control-q>', root.quit)
root.bind('<Control-t>', new_file)
root.bind('<Control-g>', open_file)
root.bind('<Control-a>', choose_select_option)
root.bind('<Control-b>', clear)


root.config(menu=menu_bar)
root.mainloop()
