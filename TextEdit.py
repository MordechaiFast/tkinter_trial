import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

window = tk.Tk()
window.title("Simple text editor")

text = tk.Text()
text.pack(expand=True, fill='both')

def open_file():
    filepath = askopenfilename(filetypes=[
        ('All Files', '*.*'), 
        ('Text Files', '*.txt'), 
        ('Python Code Files', '*.py'), 
    ])
    if filepath:
        text.delete('1.0', tk.END)
        with open(filepath) as input_file:
            text.insert(tk.END, input_file.read())
        window.title(f"Simple text editor - {filepath}")

def save_file():
    filepath = asksaveasfilename(
        defaultextension='.txt', 
        filetypes=[
            ('All Files', '*.*'), 
            ('Text Files', '*.txt'), 
            ('Python Code Files', '*.py'), 
        ]
    )
    if filepath:
        with open(filepath, mode='w') as output_file:
            output_file.write(text.get('1.0', tk.END))
        window.title(f"Simple text editor - {filepath}")

menu_bar = tk.Menu()
file_menu = tk.Menu(master=menu_bar)
file_menu.add_command(label='Open...', command=open_file)
file_menu.add_command(label='Save as...', command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=quit)
menu_bar.add_cascade(label='File', menu=file_menu)
window.config(menu=menu_bar)

window.mainloop()