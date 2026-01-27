# ================= IMPORTS =================
import tkinter as tk
from tkinter import ttk
import random
import string
import math
import time
import threading
import re

# ================= CONSTANT =================
PLACEHOLDER = "Enter Password"

# ================= ENTROPY CALCULATION =================
def calculate_entropy(password):
    pool = 0
    if re.search(r"[a-z]", password): pool += 26
    if re.search(r"[A-Z]", password): pool += 26
    if re.search(r"[0-9]", password): pool += 10
    if re.search(r"[^a-zA-Z0-9]", password): pool += 32

    if pool == 0:
        return 0

    return round(math.log2(pool ** len(password)), 2)

# ================= MATRIX VARIABLES =================
matrix_running = False
drops = []

# ================= MATRIX BACKGROUND FUNCTIONS =================
def start_matrix():
    global matrix_running, drops
    matrix_running = True
    canvas.place(x=0, y=0, relwidth=1, relheight=1)

    columns = root.winfo_width() // 15
    drops = [0 for _ in range(columns)]
    matrix_fall()

def stop_matrix():
    global matrix_running
    matrix_running = False
    canvas.place_forget()

def matrix_fall():
    if not matrix_running:
        return

    canvas.delete("all")
    chars = "01ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i in range(len(drops)):
        char = random.choice(chars)
        x = i * 15
        y = drops[i] * 18

        canvas.create_text(
            x, y,
            text=char,
            fill="#00ff99",
            font=("Consolas", 14)
        )

        if y > root.winfo_height() or random.random() > 0.95:
            drops[i] = 0
        else:
            drops[i] += 1

    root.after(70, matrix_fall)

# ================= PASSWORD ANALYSIS =================
def analyze_password():
    password = entry.get()
    entropy = calculate_entropy(password)
    strength = min(int(entropy * 1.2), 100)

    progress['value'] = strength
    percent_label.config(text=f"{strength}%")
    entropy_label.config(text=f"Entropy: {entropy} bits")

    if entropy < 40:
        result_label.config(text="WEAK ⚠ SYSTEM VULNERABLE", fg="red")
    elif entropy < 70:
        result_label.config(text="MEDIUM ⚠ HARDEN REQUIRED", fg="orange")
    else:
        result_label.config(text="STRONG ✅ MILITARY GRADE", fg="#00ff99")

# ================= FAKE HACKING LOGS =================
log_messages = [
    "[+] Initializing security modules...",
    "[+] Checking dictionary patterns...",
    "[+] Analyzing entropy vectors...",
    "[+] Evaluating brute-force resistance...",
    "[✓] Scan completed successfully"
]

def run_logs():
    logs_box.config(state="normal")
    logs_box.delete("1.0", tk.END)

    for msg in log_messages:
        logs_box.insert(tk.END, msg + "\n")
        logs_box.see(tk.END)
        time.sleep(0.5)

    logs_box.config(state="disabled")

# ================= SCANNING PROCESS =================
def hacker_scan():
    pwd = entry.get()

    if pwd == PLACEHOLDER or len(pwd) < 6:
        result_label.config(
            text="ERROR ❌ Minimum 6 characters required",
            fg="red"
        )
        progress['value'] = 0
        percent_label.config(text="0%")
        entropy_label.config(text="Entropy: 0 bits")
        return

    start_matrix()
    result_label.config(text="SCANNING SYSTEM", fg="#00ff99")

    run_logs()

    stop_matrix()
    analyze_password()

def start_scan():
    threading.Thread(target=hacker_scan).start()

# ================= PASSWORD GENERATOR =================
def generate_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*()_+=-"
    pwd = ''.join(random.choice(chars) for _ in range(16))

    entry.delete(0, tk.END)
    entry.insert(0, pwd)
    entry.config(fg="#00ff99", show="*")
    analyze_password()

# ================= SHOW / HIDE PASSWORD =================
def toggle_visibility():
    if entry.cget("show") == "":
        entry.config(show="*")
        eye_btn.config(text="👁")
    else:
        entry.config(show="")
        eye_btn.config(text="🙈")

# ================= PLACEHOLDER HANDLING =================
def on_focus_in(event):
    if entry.get() == PLACEHOLDER:
        entry.delete(0, tk.END)
        entry.config(fg="#00ff99", show="*")

def on_focus_out(event):
    if entry.get() == "":
        entry.insert(0, PLACEHOLDER)
        entry.config(fg="grey", show="")

# ================= GUI =================
root = tk.Tk()
root.title("Advanced Password Analyzer")
root.geometry("900x700")
root.configure(bg="#050d0d")

# ================= CENTER CONTAINER =================
center = tk.Frame(root, bg="#050d0d")
center.place(relx=0.5, rely=0.5, anchor="center")

tk.Label(
    center,
    text="ADVANCED PASSWORD ANALYZER",
    font=("Consolas", 22, "bold"),
    bg="#050d0d",
    fg="#00ff99"
).pack(pady=15)

frame = tk.Frame(center, bg="#050d0d")
frame.pack()

entry = tk.Entry(
    frame,
    font=("Consolas", 15),
    width=28,
    bg="black",
    fg="grey",
    insertbackground="#00ff99"
)
entry.insert(0, PLACEHOLDER)
entry.bind("<FocusIn>", on_focus_in)
entry.bind("<FocusOut>", on_focus_out)
entry.grid(row=0, column=0, padx=5)

eye_btn = tk.Button(
    frame,
    text="👁",
    bg="black",
    fg="#00ff99",
    bd=0,
    command=toggle_visibility
)
eye_btn.grid(row=0, column=1)

tk.Button(
    center,
    text="▶ START SCAN",
    font=("Consolas", 13),
    bg="black",
    fg="#00ff99",
    width=24,
    command=start_scan
).pack(pady=12)

progress = ttk.Progressbar(center, length=380, maximum=100)
progress.pack(pady=10)

percent_label = tk.Label(
    center,
    text="0%",
    font=("Consolas", 14),
    bg="#050d0d",
    fg="#00ff99"
)
percent_label.pack()

entropy_label = tk.Label(
    center,
    text="Entropy: 0 bits",
    font=("Consolas", 12),
    bg="#050d0d",
    fg="#00ff99"
)
entropy_label.pack(pady=4)

result_label = tk.Label(
    center,
    text="",
    font=("Consolas", 14, "bold"),
    bg="#050d0d"
)
result_label.pack(pady=10)

# ================= LOGS BOX =================
logs_box = tk.Text(
    center,
    height=6,
    width=52,
    bg="black",
    fg="#00ff99",
    font=("Consolas", 10),
    bd=0
)
logs_box.pack(pady=6)
logs_box.config(state="disabled")

tk.Button(
    center,
    text="⚡ GENERATE SECURE PASSWORD",
    font=("Consolas", 13),
    bg="black",
    fg="#00ff99",
    width=34,
    command=generate_password
).pack(pady=10)

# ================= MATRIX CANVAS =================
canvas = tk.Canvas(
    root,
    bg="black",
    highlightthickness=0
)

root.mainloop()
