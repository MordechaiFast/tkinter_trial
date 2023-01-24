import tkinter as tk

window = tk.Tk()

for i in range(3):
    window.columnconfigure(i, minsize=75, weight=1)
    window.rowconfigure(i, minsize=50, weight=1)
    for j in range(3):
        frame = tk.Frame(relief=tk.RAISED, borderwidth=1)
        frame.grid(row=i, column=j, padx=5, pady=5)
        tk.Label(frame, text=f'Row {i} \nColumn {j}').pack(padx=5, pady=5)

window.mainloop()