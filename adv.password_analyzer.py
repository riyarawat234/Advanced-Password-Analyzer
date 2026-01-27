import tkinter as tk
import random
import string

# ===== 1. FUNCTIONS FIRST (root से PEHLE) =====
def toggle_show():
    if show_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

def analyze_password():
    password = password_entry.get()
    length_score = 0
    if len(password) >= 12: length_score = 30
    elif len(password) >= 8: length_score = 20
    else: length_score = 10
    
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)
    
    score = length_score
    if has_upper: score += 20
    if has_lower: score += 10
    if has_digit: score += 20
    if has_special: score += 20
    
    progress.config(text=f"Strength: {score}%")
    
    if score >= 80:
        strength_label.config(text="VERY STRONG", fg="#00ff88")
    elif score >= 50:
        strength_label.config(text="MEDIUM", fg="#ffdd59")
    else:
        strength_label.config(text="WEAK", fg="#ff4757")

def generate_password():
    length = int(length_var.get())
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    new_pwd = ''.join(random.choice(chars) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, new_pwd)
    analyze_password()

# ===== 2. MAIN WINDOW (functions के बाद) =====
root = tk.Tk()
root.title("🔐 Advanced Password Analyzer - Cybersecurity Tool")
root.geometry("500x700")
root.resizable(False, False)

# Header
tk.Label(root, text="🔐 ADVANCED PASSWORD ANALYZER", 
         font=("Arial", 20, "bold"), fg="#00d4ff", bg="#1a1a2e").pack(pady=20)

# Input section
tk.Label(root, text="Enter Password:", font=("Arial", 14), 
         fg="white", bg="#1a1a2e").pack(pady=5)

# नया shiny entry (title_frame के बाद):
entry_frame = tk.Frame(root, bg="#1a1a2e", relief="ridge", bd=3)
entry_frame.pack(pady=20, padx=40, fill="x")

password_entry = tk.Entry(entry_frame, font=("Arial", 14), width=35, 
                         show="*", justify="center", 
                         bg="#2a2a3e", fg="cyan",
                         relief="flat", bd=5,
                         insertbackground="cyan",
                         selectbackground="#00d4ff")
password_entry.pack(pady=12)
show_var = tk.BooleanVar()
show_btn = tk.Checkbutton(entry_frame, text="Show Password", 
                         variable=show_var, bg="#1a1a2e", 
                         fg="white", selectcolor="#2a2a3e",
                         font=("Arial", 11))
show_btn.pack()


# Show/Hide password
def toggle_show():
    if show_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

show_var = tk.BooleanVar()
show_btn = tk.Checkbutton(root, text="Show Password 👁️", variable=show_var, 
                         command=toggle_show, bg="#1a1a2e", fg="white", 
                         selectcolor="#16213e", font=("Arial", 10))
show_btn.pack(pady=5)

# Analyze function - MAIN LOGIC
def analyze_password():
    pwd = password_entry.get()
    if not pwd:
        result_label.config(text="❌Enter Password!", fg="red")
        return
    
    score = 0
    feedback = []
    
    # Length check
    if len(pwd) >= 12: 
        score += 2
        feedback.append("✅ Length: Excellent (12+)")
    elif len(pwd) >= 8:
        score += 1
        feedback.append("✅ Length: Good (8-11)")
    else:
        feedback.append("❌ Length: Weak (<8)")
    
    # Character checks
    if re.search(r"[a-z]", pwd):
        score += 1
        feedback.append("✅ Lowercase: ✓")
    else:
        feedback.append("❌ Lowercase missing")
    
    if re.search(r"[A-Z]", pwd):
        score += 1
        feedback.append("✅ Uppercase: ✓")
    else:
        feedback.append("❌ Uppercase missing")
    
    if re.search(r"\d", pwd):
        score += 1
        feedback.append("✅ Numbers: ✓")
    else:
        feedback.append("❌ Numbers missing")
    
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", pwd):
        score += 1
        feedback.append("✅ Special chars: ✓")
    else:
        feedback.append("❌ Special chars missing")
    
    # Final result
    if score >= 8: strength = "🟢 VERY STRONG"; color = "green"
    elif score >= 6: strength = "🟡 STRONG"; color = "orange"
    elif score >= 4: strength = "🟡 MEDIUM"; color = "yellow"
    else: strength = "🔴 WEAK"; color = "red"
    
    result = f"{strength}\nScore: {score}/7\n\n" + "\n".join(feedback[:6])
    result_label.config(text=result, fg=color)
    
    # Progress bar update
    progress['value'] = score * 14  # Max 100

# Buttons
analyze_btn = tk.Button(root, text="🔍 ANALYZE PASSWORD", 
                       command=analyze_password, 
                       bg="#00d4ff", fg="black",
                       font=("Arial", 14, "bold"), 
                       width=22, height=2,
                       relief="flat", bd=0,
                       activebackground="#00b8d4")
analyze_btn.pack(pady=20)

# generator label + button:
tk.Label(root, text="Generate Strong Password:", 
         font=("Arial", 14), fg="cyan", bg="#0f0f23").pack(pady=(20,5))

gen_btn = tk.Button(root, text="🎲 GENERATE STRONG PASSWORD", 
                   command=generate_password, 
                   bg="#ff4757", fg="white",
                   font=("Arial", 12, "bold"), 
                   width=28, height=2,
                   relief="flat", bd=0,
                   activebackground="#ff3742")
gen_btn.pack(pady=10)

# progress label को:
progress_frame = tk.Frame(root, bg="#16213e", relief="ridge", bd=2)
progress_frame.pack(pady=15, padx=30, fill="x")
progress = tk.Label(progress_frame, text="Strength: 0%", 
                   font=("Arial", 16, "bold"), fg="white", bg="#16213e")
progress.pack(pady=10)

strength_label = tk.Label(root, text="MEDIUM", font=("Arial", 18, "bold"), fg="#ffdd59")
strength_label.pack(pady=5)


# Result area
result_label = tk.Label(root, text="Result:\nAnalyze Password!", 
                       font=("Arial", 12), bg="#1a1a2e", fg="#ecf0f1",
                       justify="left", wraplength=450)
result_label.pack(pady=20)

root.mainloop()
