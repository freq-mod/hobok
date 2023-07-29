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
        if len(password)>temp_len.get()-2:
            break
    output_pass.set(password)

window=Tk()
output_pass = StringVar()
window.geometry("320x240")
window.title="password generator"

label= Label(window, text = 'Length', font = 'PC-9800').pack(pady=10)
temp_len = IntVar()
length= Spinbox(window, from_ =0, to_=32, increment=3, textvariable = temp_len , width = 20, font='PC-9800').pack()

Button(window, text = "Generate" , command = passgen, font="PC-9800", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)
pass_label = Label(window, text = 'password:', font = 'PC-9800').pack(pady="20 10")
Entry(window , textvariable = output_pass, width = 24, font='PC-9800').pack()

window.mainloop()