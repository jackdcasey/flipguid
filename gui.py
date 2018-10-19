#TODO: Make GUI look better, add convert on hitting enter 

import logic as fn 
from tkinter import *

def flipinput():
    output.delete(0, END)
    converted = fn.flipguid(input.get())
    output.insert(0, converted)

def copytoclipboard():
    win.clipboard_clear()
    win.clipboard_append(output.get())

def pastefromclipboard():
    input.delete(0, END)
    input.insert(0, win.clipboard_get())

win = Tk()
win.title("FlipGUID")

inputlabel = Label(win, text="Input: ")
input = Entry(win, bg='#eee', bd=0, width=40)
output = Entry(win, bg='#eee', bd=0, width=40)
convertbutton = Button(win, text='Convert', command=flipinput)
copybutton = Button(win, text='Copy to clipboard', command=copytoclipboard)
pastebutton = Button(win, text='Paste from clipboard', command=pastefromclipboard)

inputlabel.grid(row=0, padx=(10, 20), pady=(7, 7))
input.grid(row=0, column=1, padx=(10, 20), pady=(7, 7))
output.grid(row=1, column=1, padx=(10, 20), pady=(7, 7))
convertbutton.grid(row=1, padx=(10, 20), pady=(7, 7))
copybutton.grid(row=1, column=2, padx=(10, 20), pady=(7, 7))
pastebutton.grid(row=0, column=2, padx=(10, 20), pady=(7, 7))

win.mainloop()
