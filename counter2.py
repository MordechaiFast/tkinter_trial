import tkinter as tk

def increase():
    value_lbl['text'] = str(int(value_lbl['text']) + 1)
def decrease():
    value_lbl['text'] = str(int(value_lbl['text']) - 1)

window = tk.Tk()

window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)
tk.Button(text='-', command=decrease).grid(row=0, column=0, sticky='nsew')
value_lbl = tk.Label(text='0')
value_lbl.grid(row=0, column=1)
tk.Button(text='+', command=increase).grid(row=0, column=2, sticky='nsew')

window.mainloop()
