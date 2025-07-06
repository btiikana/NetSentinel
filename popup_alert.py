import tkinter as tk
from tkinter import messagebox

def show_block_popup(ip, location):
    root = tk.Tk()
    root.withdraw()
    message = f"Blocked IP: {ip}\nLocation: {location}\n\nThe attack has been stopped."
    messagebox.showinfo("Attack Blocked!", message)
    root.destroy()
