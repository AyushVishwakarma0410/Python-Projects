import tkinter as tk


root = tk.Tk()

root.title("practice")
root.geometry("1000x1000")
label = tk.Label(root,text="hello")

label.place(x=500,y=100)

root.mainloop()