from tkinter import *
import secrets
import string

def passgen():
    password=""
    for i in range(temp_len.get()):
        letter=secrets.choice(string.ascii_letters)
        digit=secrets.choice(string.digits)
        punctuation=secrets.choice(string.punctuation)
        password += letter + digit + punctuation
        if len(password)>temp_len.get():
            password=password[:temp_len.get()]
            break
    output_pass.set(password)

window=Tk()
output_pass = StringVar()
window.geometry("384x272")
window.configure(bg='lightblue')
window.title("password generator")
font_str = "PC-9800 12"

label= Label(window, text = 'Length', font = font_str, bg='lightblue').pack(pady=10)
temp_len = IntVar()
length= Spinbox(window, from_ =0, to_=32, textvariable = temp_len , width = 20, font=font_str).pack()

Button(window, text = "Generate" , command = passgen, font=font_str, bg='lightgreen', fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)
pass_label = Label(window, text = 'password:', font = font_str, bg='lightblue').pack(pady="20 10")
Entry(window , textvariable = output_pass, width = 24, font=font_str).pack()

window.mainloop()