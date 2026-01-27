import tkinter as tk

root = tk.Tk()
root.title("Password Analyzer v2")
root.geometry("450x400")
root.configure(bg="#2c3e50")

# Title
tk.Label(root, text="🔐 ADVANCED PASSWORD ANALYZER", 
         font=("Arial", 18, "bold"), fg="white", bg="#2c3e50").pack(pady=20)

# Password input
tk.Label(root, text="Password enter karo:", font=("Arial", 14), 
         fg="white", bg="#2c3e50").pack(pady=5)
password_entry = tk.Entry(root, width=30, font=("Arial", 12), show="*", 
                         bg="white", relief="solid", bd=2)
password_entry.pack(pady=10)

# Analyze button
def check_password():
    pwd = password_entry.get()
    if pwd:
        length = len(pwd)
        if length >= 12:
            result = "🚀 EXCELLENT! Bahut strong password"
        elif length >= 8:
            result = "✅ GOOD! Thik hai"
        else:
            result = "⚠️ WEAK! 8+ characters karo"
        result_label.config(text=result, fg="green")
    else:
        result_label.config(text="Password enter karo pehle!", fg="orange")

btn = tk.Button(root, text="ANALYZE 🔍", command=check_password, 
                bg="#27ae60", fg="white", font=("Arial", 12, "bold"),
                width=15, relief="raised", bd=3)
btn.pack(pady=20)

# Result display
result_label = tk.Label(root, text="Result yaha dikhega...", 
                       font=("Arial", 14), bg="#2c3e50", fg="#ecf0f1")
result_label.pack(pady=20)

root.mainloop()
