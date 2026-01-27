import tkinter as tk

window = tk.Tk()
window.title("Simple GUI")
window.geometry("300x200")

label = tk.Label(window, text="Hello!", font=("Arial", 20))
label.pack(pady=50)

def click():
    label.config(text="Button Clicked!")

button = tk.Button(window, text="Click Me", command=click, bg="blue", fg="white")
button.pack()

window.mainloop()