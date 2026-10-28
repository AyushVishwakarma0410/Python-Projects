import tkinter as tk


root = tk.Tk()

root.geometry("400x500")
root.title("Calculator")



label1 = tk.Label(root,text="Enter first Number :")
label1.pack()
entry = tk.Entry(root)
entry.delete(0,tk.END)
entry.pack(pady=5)

label2 = tk.Label(root,text="Enter Second number :")
label2.pack()
entry2 = tk.Entry(root)
entry2.delete(0,tk.END)
entry2.pack(pady=5)


def add():
    try :
        first = int(entry.get())
        second = int(entry2.get())
    except ValueError:
        result_label.config(text="Error : Please enter a valid number",fg="red",bg="black") 
        return     

    result =  first + second
    result_label.config(text=f"Result : {result}",fg="green",bg="white")

def substract():
    try :
        first = int(entry.get())
        second = int(entry2.get())
    except ValueError:
        result_label.config(text="Error : Please enter a valid number",fg="red",bg="black")
        return
    
    result = first - second
    result_label.config(text=f"Result : {result}",fg="green",bg="white") 

def multiply():
    try :
        first = int(entry.get())
        second = int(entry2.get())
    except ValueError:
        result_label.config(text="Error : Please enter a valid number",fg="red",bg="black")
        return
    
    result = first * second
    result_label.config(text=f"Result : {result}",fg="green",bg="white") 

def divide():
    try :
        first = int(entry.get())
        second = int(entry2.get())
    except ValueError:
        result_label.config(text="Error : Please enter a valid number",fg="red",bg="black")
        return
    
    result = first / second
    result_label.config(text=f"Result : {result}",fg="green",bg="white") 


def modulo():
    try :
        first = int(entry.get())
        second = int(entry2.get())
    except ValueError:
        result_label.config(text="Error : Please enter a valid number",fg="red",bg="black")
        return

    result = first % second
    result_label.config(text=f"Result : {result}",fg="green",bg="white")    

button = tk.Button(root,text="Press to add",command=add)
button.pack(pady=5)

button_subs = tk.Button(root,text="Press to substract",command=substract)
button_subs.pack(pady=5)

button_mult = tk.Button(root,text="Press to multiply",command=multiply)
button_mult.pack(pady=5)

button_div = tk.Button(root,text="Press to divide",command=divide)
button_div.pack(pady=5)

button_div = tk.Button(root,text="Press to mod",command=modulo)
button_div.pack(pady=5)

result_label = tk.Label(root,text="")
result_label.pack(pady=10)




def clear():
    entry.delete(0,tk.END)
    entry2.delete(0,tk.END)
    result_label.config(text="",fg="black",bg=root.cget("bg"))

clear_button = tk.Button(root,text="Clear",command=clear)
clear_button.pack(pady=5)
root.mainloop()