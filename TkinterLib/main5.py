import tkinter as tk



root = tk.Tk()
root.geometry("400x100")

label1 = tk.Label(root,text="Hello")
label2 = tk.Label(root,text="World")

entry = tk.Entry(root)
entry2 = tk.Entry(root)


label1.grid(row = 0, column = 0)
entry.grid(row = 0, column = 1)

label2.grid(row = 1, column = 0)
entry2.grid(row = 1, column = 1)



root.mainloop()