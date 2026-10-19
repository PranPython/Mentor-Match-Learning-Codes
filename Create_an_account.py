import tkinter as tk

scr = tk.Tk()
scr.geometry("500x500")

# Creating a title
scr.title("Sign up")

sign_up = tk.Label(scr,text = "Sign up", font = ("times new roman",30),fg = "black")
sign_up.pack()

def sign():
    name_store = name_inp.get()
    e_store = email_inp.get()
    user_store = user_inp.get()
    pass_store = password_inp.get()
    if name_store == "" or e_store == "" or user_store == "" or pass_store == "":
        ent_all_fld.config(text = "*Please Fill in all the Fields*")
    else:
        savin = open('account-saving.txt','a')
        savin.write(name_store + "," + e_store + "," + user_store + "," + pass_store + "\n" )
        savin.close()
        ent_all_fld.config(text = "*Account created Successfully")
        name_inp.delete(0,tk.END)
        email_inp.delete(0,tk.END)
        user_inp.delete(0,tk.END)
        password_inp.delete(0,tk.END)


name = tk.Label(scr,text = "Name", font = ("Arial",15),fg = "Black",bg = "white")
name.place(x = 200, y = 60)

name_inp = tk.Entry(scr, font = ("Arial",15),fg = "black")
name_inp.place(x = 120,y = 100)

email = tk.Label(scr,text = "Email", font = ("Arial",15),fg = "Black",bg = "white")
email.place(x = 200, y = 140)

email_inp = tk.Entry(scr, font = ("Arial",15),fg = "black")
email_inp.place(x = 120,y = 180)

user = tk.Label(scr,text = "Username", font = ("Arial",15),fg = "Black",bg = "white")
user.place(x = 185, y = 220)

user_inp = tk.Entry(scr, font = ("Arial",15),fg = "black")
user_inp.place(x = 120,y = 260)

password = tk.Label(scr,text = "Password", font = ("Arial",15),fg = "Black",bg = "white")
password.place(x = 200, y = 300)

password_inp = tk.Entry(scr,show = "*", font = ("Arial",15),fg = "black")
password_inp.place(x = 120,y = 340)

sign_up = tk.Button(scr, text = "Sign up", font = ("Arial",20), fg = "Black",command = sign)
sign_up.place(x = 175,y = 400)

ent_all_fld = tk.Label(scr,text = "" ,font = ("Times New Roman",20),fg = "red")
ent_all_fld.place(x = 95,y = 450)


scr.mainloop()