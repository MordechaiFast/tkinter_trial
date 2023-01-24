import tkinter as tk
window = tk.Tk()
msg = tk.Label(text="Whatever you type while this window is open gets recorded,"
    " even though you don't have any way of knowing.")
msg.pack()
typing = ''

def record(event):
    global typing
    if event.char == '\r':
        print(typing)
        window.destroy()
    typing += event.char

window.bind('<Key>', record)
window.mainloop()