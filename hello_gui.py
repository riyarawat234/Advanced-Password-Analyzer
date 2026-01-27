import tkinter as tk

root = tk.Tk()
root.title("My First GUI")
root.geometry("300x200")

# add a label
label = tk.Label(root, text="Hello, Welcome to GUI!", font=("Arial", 14))
label.pack(pady=20)
root.mainloop()
