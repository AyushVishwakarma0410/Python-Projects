import tkinter as tk


root = tk.Tk()
root.title("Frame Example")
root.geometry("400x300")


#create frame 
input_frame = tk.Frame(root,padx=10,pady=10)
input_frame.grid(row=0,column=0)


#Put widgets inside the frame 
label = tk.Label(input_frame,text="Enter your name :")
label.grid(row = 0, column = 0, padx=5, pady=5)

entry = tk.Entry(input_frame)
entry.grid(row=0, column=1, padx=5, pady=5)

def greet():
    name = entry.get()
    result_label.config(text=f"Hello,{name}!")

button = tk.Button(input_frame, text="Great", command=greet)
button.grid(row=1,column=0,columnspan=2,pady=5)

result_label = tk.Label(root,text="")
result_label.grid(row=1,column=1,pady=10)



#Second frame
input_frame2 = tk.Frame(root,padx=20,pady=20)
input_frame2.grid(row=1,column=0,pady=10)

#putting a label in second frame

result_label = tk.Label(input_frame2,text="Hello")
result_label.grid(row = 0, column = 0, padx = 5, pady = 5)




root.mainloop()