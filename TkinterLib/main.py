import tkinter as tk


# Main application window
root = tk.Tk()

# Set the window title
root.title("My First GUI")

# Set the window dimensions 
root.geometry("400x300")

# Create a label 
label = tk.Label(root, text="Hello, Tkinter!")

# Display the label
label.pack()

# Start the application's event loop
root.mainloop()
