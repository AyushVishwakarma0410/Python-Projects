import tkinter as tk


root = tk.Tk()
root.title("Interactive GUI")
root.geometry("400x300")

def say_hello():
    label.config(text="Hello! You clicked the button")


label = tk.Label(root,text = "Click the button")
label.pack(pady=20)

button = tk.Button(root,
                   text="Click",
                   command=say_hello
                   )
button.pack()
root.mainloop()