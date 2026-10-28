import tkinter as tk

root = tk.Tk()
root.title("Widget Demo")
root.geometry("400x300")

label = tk.Label(root, text="Welcome to Tkinter")
label.pack()


button = tk.Button(root,text="Click me")
button.pack()

root.mainloop()