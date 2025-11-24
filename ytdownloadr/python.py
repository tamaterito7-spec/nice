from tkinter import *
import tkinter.filedialog as fd
import tkinter.messagebox as mb
from PIL import Image, ImageTk  # <-- Fixed: Import Image
import os

# Global variable to track current file
current_file = None

# Initialize main window
root = Tk()
root.title("Untitled - Notepad")
root.geometry('800x500')
root.resizable(0, 0)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Set icon (with error handling)
try:
    icon = ImageTk.PhotoImage(Image.open('Notepad.png'))
    root.iconphoto(False, icon)
except Exception as e:
    print(f"Icon not found: {e}")

# Text area with scrollbar
text_area = Text(root, font=("Times New Roman", 12), undo=True)
text_area.grid(row=0, column=0, sticky=NSEW)

scroller = Scrollbar(root, orient=VERTICAL, command=text_area.yview)
scroller.grid(row=0, column=1, sticky=NS)
text_area.config(yscrollcommand=scroller.set)

# === Functions ===

def open_file():
    global current_file
    file = fd.askopenfilename(
        defaultextension='.txt',
        filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')]
    )
    if file:
        current_file = file
        root.title(f"{os.path.basename(file)} - Notepad")
        text_area.delete(1.0, END)
        with open(file, "r", encoding="utf-8") as f:
            text_area.insert(1.0, f.read())

def new_file():
    global current_file
    current_file = None
    root.title("Untitled - Notepad")
    text_area.delete(1.0, END)

def save_file():
    global current_file
    if current_file:
        with open(current_file, "w", encoding="utf-8") as f:
            f.write(text_area.get(1.0, END).rstrip())
        root.title(f"{os.path.basename(current_file)} - Notepad")
    else:
        save_as_file()

def save_as_file():
    global current_file
    file = fd.asksaveasfilename(
        initialfile="Untitled.txt",
        defaultextension=".txt",
        filetypes=[
            ("Text Document", "*.txt"),
            ("All Files", "*.*")
        ]
    )
    if file:
        current_file = file
        with open(file, "w", encoding="utf-8") as f:
            f.write(text_area.get(1.0, END).rstrip())
        root.title(f"{os.path.basename(file)} - Notepad")

def exit_application():
    if mb.askyesno("Quit", "Do you want to save before quitting?"):
        save_file()
    root.destroy()

def copy_text():
    text_area.event_generate("<<Copy>>")

def cut_text():
    text_area.event_generate("<<Cut>>")

def paste_text():
    text_area.event_generate("<<Paste>>")

def select_all():
    text_area.tag_add('sel', '1.0', 'end')

def delete_last_char():
    text_area.delete("end-2c")

def about_notepad():
    mb.showinfo("About Notepad", "This is a simple Notepad clone made with Tkinter & PIL.\nBetter than the original? You decide!")

def about_commands():
    commands = """
File Menu:
  New           - Clears text area
  Open          - Opens a text file
  Save As       - Saves file with chosen name
  Exit          - Closes the app

Edit Menu:
  Copy          - Copies selected text
  Cut           - Cuts selected text
  Paste         - Pastes from clipboard
  Select All    - Selects all text
  Delete        - Deletes last character

Help Menu:
  About         - Info about this app
  Commands      - This help dialog
    """
    mb.showinfo("Commands Help", commands)

# === Menu Bar ===
menu_bar = Menu(root)

# File Menu
file_menu = Menu(menu_bar, tearoff=False)
file_menu.add_command(label="New", command=new_file, accelerator="Ctrl+N")
file_menu.add_command(label="Open", command=open_file, accelerator="Ctrl+O")
file_menu.add_command(label="Save", command=save_file, accelerator="Ctrl+S")
file_menu.add_command(label="Save As...", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_application)
menu_bar.add_cascade(label="File", menu=file_menu)

# Edit Menu
edit_menu = Menu(menu_bar, tearoff=False)
edit_menu.add_command(label="Undo", command=text_area.edit_undo, accelerator="Ctrl+Z")
edit_menu.add_command(label="Redo", command=text_area.edit_redo, accelerator="Ctrl+Y")
edit_menu.add_separator()
edit_menu.add_command(label="Cut", command=cut_text, accelerator="Ctrl+X")
edit_menu.add_command(label="Copy", command=copy_text, accelerator="Ctrl+C")
edit_menu.add_command(label="Paste", command=paste_text, accelerator="Ctrl+V")
edit_menu.add_separator()
edit_menu.add_command(label="Select All", command=select_all, accelerator="Ctrl+A")
edit_menu.add_command(label="Delete Last Char", command=delete_last_char)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Help Menu
help_menu = Menu(menu_bar, tearoff=False)
help_menu.add_command(label="About Notepad", command=about_notepad)
help_menu.add_command(label="Commands", command=about_commands)
menu_bar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu_bar)

# Keyboard shortcuts
root.bind_all("<Control-n>", lambda e: new_file())
root.bind_all("<Control-o>", lambda e: open_file())
root.bind_all("<Control-s>", lambda e: save_file())
root.bind_all("<Control-a>", lambda e: select_all())

# Start the app
root.mainloop()