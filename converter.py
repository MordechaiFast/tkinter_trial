"""Celsius to Fahrenheit converter"""
import tkinter as tk

def CtoF():
    celsius = temp_ent.get()
    fahrenheit = 9 / 5 * float(celsius) + 32
    result_lbl['text'] = f'{round(fahrenheit, 2)} \N{DEGREE FAHRENHEIT}'

def FtoC():
    fahrenheit = temp_ent.get()
    celsius = 5 / 9 * (float(fahrenheit) - 32)
    result_lbl['text'] = f'{round(celsius, 2)} \N{DEGREE CELSIUS}'

def convert():
    if toF:
        CtoF()
    else:
        FtoC()

def catch_enter(event):
    if event.char == '\r':
        convert()

def set_CtoF():
    global toF
    toF = True
    temp_lbl['text'] = '\N{DEGREE CELSIUS}'
    result_lbl['text'] = '\N{DEGREE FAHRENHEIT}'

def set_FtoC():
    global toF
    toF = False
    temp_lbl['text'] = '\N{DEGREE FAHRENHEIT}'
    result_lbl['text'] = '\N{DEGREE CELSIUS}'

window = tk.Tk()
window.title('Temperature converter')
window.resizable(width=False, height=False)

entry_frm = tk.Frame()
temp_ent = tk.Entry(master=entry_frm, width=10)
temp_ent.grid(row=0, column=0, sticky='e')
temp_lbl = tk.Label(master=entry_frm)
temp_lbl.grid(row=0, column=1, sticky='w')
entry_frm.grid(row=0, column=0, padx=10)

tk.Button(
    text='\N{RIGHTWARDS BLACK ARROW}', 
    command=convert
).grid(row=0, column=1, padx=10)

result_lbl = tk.Label()
result_lbl.grid(row=0, column=2, padx=10)

window.bind('<Key>', catch_enter)

menu_bar = tk.Menu()
file_menu = tk.Menu(master=menu_bar)
file_menu.add_command(
    label='\N{DEGREE CELSIUS} to \N{DEGREE FAHRENHEIT}', 
    command=set_CtoF
)
file_menu.add_command(
    label='\N{DEGREE FAHRENHEIT} to \N{DEGREE CELSIUS}', 
    command=set_FtoC
)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=quit)
menu_bar.add_cascade(label='File', menu=file_menu)
window.config(menu=menu_bar)

set_CtoF()

window.mainloop()