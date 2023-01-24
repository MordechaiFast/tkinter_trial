import tkinter as tk
window = tk.Tk()
msg = tk.Label(text="Hello, tk! This is Python. What is the user's name?")
msg.pack()
qu = tk.Entry()
qu.pack()

def look_for_enter(event):
    if event.char == '\r':
        print(f'The user\'s name was "{qu.get()}".')
        window.destroy()

window.bind('<Key>', look_for_enter)
window.mainloop()
