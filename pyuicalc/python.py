#import
#def window
#def text and math
#place ui elements
#ok button
from tkinter import * 
from tkinter.messagebox import showerror

root = Tk()
root.title("PythonGeeks Calculator")
root.geometry('265x500')
root.resizable(0, 0)
root.configure(background='LightCyan2')

entry_strvar = StringVar(root)

Label(root, text='PythonGeeks Calculator', font=("Comic Sans MS", 15), 
      bg="LightCyan2").place(x=25, y=0)

Label(root, text="Press \'x\' twice for exponentiation", font=("Georgia", 10),
      bg="LightCyan2").place(x=30, y=30)

eqn_entry = Entry(root, justify=RIGHT, textvariable=entry_strvar, width=22, font=12,
                  state='disabled')
eqn_entry.place(x=10, y=70)

root.update()


def add_text(text, strvar: StringVar):
    strvar.set(f'{strvar.get()}{text}')

def submit(entry: Entry, strvar: StringVar):
    operation = entry.get()
    try:
        strvar.set(f'{strvar.get()}={eval(operation)}')
    except:
        showerror('Error!', 'Please enter a properly defined equation!')

Button(root, height=2, width=5, text='7', font=9, bg='Gold', command=lambda:
       add_text("7", entry_strvar)).place(x=5, y=170)

Button(root, height=2, width=5, text='8', font=9, bg='Gold', command=lambda:
       add_text("8", entry_strvar)).place(x=65, y=170)

Button(root, height=2, width=5, text='9', font=9, bg='Gold', command=lambda:
       add_text('9', entry_strvar)).place(x=125, y=170)

Button(root, height=2, width=5, text='4', font=9, bg='Gold', command=lambda:
       add_text('4', entry_strvar)).place(x=5, y=225)

Button(root, height=2, width=5, text='5', font=9, bg='Gold', command=lambda:
       add_text('5', entry_strvar)).place(x=65, y=225)

Button(root, height=2, width=5, text='6', font=9, bg='Gold', command=lambda:
       add_text('6', entry_strvar)).place(x=125, y=225)

Button(root, height=2, width=5, text='1', font=9, bg='Gold', command=lambda:
       add_text('1', entry_strvar)).place(x=5, y=280)

Button(root, height=2, width=5, text='2', font=9, bg='Gold', command=lambda:
       add_text('2', entry_strvar)).place(x=65, y=280)

Button(root, height=2, width=5, text='3', font=9, bg='Gold', command=lambda:
       add_text('3', entry_strvar)).place(x=125, y=280)

Button(root, height=2, width=5, text='0', font=9, bg='Gold', command=lambda:
       add_text('0', entry_strvar)).place(x=5, y=340)

add = Button(root, height=2, width=5, text='+', font=9, bg='DarkOrange', command=lambda:
             add.place(x=195, y=340))

subtract = Button(root, height=2, width=5, text='-', font=9, bg='DarkOrange', command=lambda:
             subtract.place(x=195, y=280))

multiply = Button(root, height=2, width=5, text='*', font=9, bg='DarkOrange', command=lambda:
             multiply.place(x=195, y=225))

divide = Button(root, height=2, width=5, text='/', font=9, bg='DarkOrange', command=lambda:
             divide.place(x=195, y=170))

decimal = Button(root, height=2, width=5, text='.', font=9, bg='DarkOrange', command=lambda:
             decimal.place(x=65, y=340))

bracket_open = Button(root, height=2, width=5, text='.', font=9, bg='DarkOrange', command=lambda:
             bracket_open.place(x=65, y=110))

bracket_close = Button(root, height=2, width=5, text='.', font=9, bg='DarkOrange', command=lambda:
             bracket_close.place(x=125, y=110))

equal = Button(root, height=2, width=5, text='=', font=9, bg='Blue', command=lambda:
               submit(eqn_entry, entry_strvar))
equal.place(x=125, y=340)

clear = Button(root, height=2, width=5, text='C', font=9, bg='OrangeRed',
               command=lambda: entry_strvar.set(entry_strvar.get()[:-1]))

AC_btn = Button(root, height=2, width=5, text='AC', font=9, bg='Red', command=lambda:
                entry_strvar.set(''))
AC_btn.place(x=5, y=110)

ok_btn = Button(root, height=2, width=22, text='Ok', font=9, bg='CadetBlue',
                command=lambda: root.destroy())
ok_btn.place(x=7, y=420)

root.mainloop()