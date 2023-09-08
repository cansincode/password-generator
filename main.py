import string
import secrets
import pyperclip
import tkinter as tk
from tkinter import *
import pwnedpasswords
import customtkinter as ctk

# CanMgn-R Generator Page(1)
root = ctk.CTk()
root.geometry("350x175")
root.eval('tk::PlaceWindow . center')

# Password length Slider
length_int = tk.IntVar(value = 16)
length = ctk.CTkSlider(
    root,
    from_ = 8,
    to = 128,
    variable = length_int
    )
length.place(x=50, y=20)
length_value = ctk.CTkLabel(root, textvariable=length_int)
length_value.place(x=270, y=14)

# Password Input
passwd = ctk.CTkEntry(
    root,
    width = 303,
    height = 25,
    placeholder_text = "Password",
    corner_radius=20
    )
passwd.place(x=25, y=130)


# Password Generator Function
def gen():
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    alphabet = letters + digits + special
    pwdlength = int(length.get())
    password = ''
    password = ''.join(str(secrets.choice(alphabet)) for i in range(pwdlength))
    password_ = str(password)
    pyperclip.copy(password_)
    set_text(password_)

def set_text(text):
    passwd.delete(0,END)
    passwd.insert(0,text)
    return

# Password Generator Button
genbtn = ctk.CTkButton(
    root,
    text="Generate",
    corner_radius=20,
    command=gen,
    )
genbtn.place(x=185, y=60)

# Password Leak Checker
def check():
    passwd_input = passwd.get()
    passwd_leaks = pwnedpasswords.check(passwd_input, plain_text=True)
    passwd_leaks_ = "this password leaked in", passwd_leaks, "Databases"
    clsbg = " " * 100
    clearbg = ctk.CTkLabel(root, text=clsbg)
    clearbg.place(x=25, y=95)
    passwd_sec = ctk.CTkLabel(root, text=passwd_leaks_)
    passwd_sec.place(x=25, y=95)
# Leak Checker Button
checkbtn = ctk.CTkButton(
    root,
    text="Check Leaks",
    corner_radius=20,
    command=check
    )
checkbtn.place(x=25, y=60)

root.mainloop()