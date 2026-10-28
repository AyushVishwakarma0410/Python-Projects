import tkinter as tk


root = tk.Tk()
root.title("Greeting App")
root.geometry("400x300")


def great():
    name = name_entry.get()

    if name.strip():
        result_label.config(text=f"Hello,{name}!")
    else:
        result_label.config(text="Please enter your name.")


label = tk.Label(root,text="Enter your name:")
label.pack(pady=10)

name_entry = tk.Entry(root)
name_entry.pack(pady=5)

button = tk.Button(root,text="Greet me", command=great)
button.pack(pady=10)

result_label = tk.Label(root,text="")
result_label.pack(pady=10)

root.mainloop()