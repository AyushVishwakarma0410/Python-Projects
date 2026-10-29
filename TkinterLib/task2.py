
import tkinter as tk

root = tk.Tk()
root.geometry("400x500")
root.title("Calculator")

label1 = tk.Label(root, text="Enter first Number:")
label1.grid(row=0, column=0, padx=5, pady=5)

entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=5, pady=5)

label2 = tk.Label(root, text="Enter Second number:")
label2.grid(row=1, column=0, padx=5, pady=5)

entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=5, pady=5)

result_label = tk.Label(root, text="")
result_label.grid(row=5, column=0, columnspan=2, pady=10)


def get_numbers():
    try:
        first = int(entry.get())
        second = int(entry2.get())
        return first, second
    except ValueError:
        result_label.config(
            text="Error: Please enter valid numbers",
            fg="red",
            bg="black"
        )
        return None


def add():
    numbers = get_numbers()
    if numbers is None:
        return

    first, second = numbers
    result = first + second
    result_label.config(text=f"Result: {result}", fg="green", bg="white")


def substract():
    numbers = get_numbers()
    if numbers is None:
        return

    first, second = numbers
    result = first - second
    result_label.config(text=f"Result: {result}", fg="green", bg="white")


def multiply():
    numbers = get_numbers()
    if numbers is None:
        return

    first, second = numbers
    result = first * second
    result_label.config(text=f"Result: {result}", fg="green", bg="white")


def divide():
    numbers = get_numbers()
    if numbers is None:
        return

    first, second = numbers

    if second == 0:
        result_label.config(text="Cannot divide by zero", fg="red")
        return

    result = first / second
    result_label.config(text=f"Result: {result}", fg="green", bg="white")


def modulo():
    numbers = get_numbers()
    if numbers is None:
        return

    first, second = numbers

    if second == 0:
        result_label.config(text="Cannot use modulo with zero", fg="red")
        return

    result = first % second
    result_label.config(text=f"Result: {result}", fg="green", bg="white")


def clear():
    entry.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_label.config(
        text="",
        fg="black",
        bg=root.cget("bg")
    )


button = tk.Button(root, text="Press to add", command=add)
button.grid(row=2, column=0, padx=5, pady=5)

button_subs = tk.Button(root, text="Press to subtract", command=substract)
button_subs.grid(row=2, column=1, padx=5, pady=5)

button_mult = tk.Button(root, text="Press to multiply", command=multiply)
button_mult.grid(row=3, column=0, padx=5, pady=5)

button_div = tk.Button(root, text="Press to divide", command=divide)
button_div.grid(row=3, column=1, padx=5, pady=5)

button_mod = tk.Button(root, text="Press to mod", command=modulo)
button_mod.grid(row=4, column=0, padx=5, pady=5)

clear_button = tk.Button(root, text="Clear", command=clear)
clear_button.grid(row=6, column=0, columnspan=2, pady=5)

root.mainloop()
