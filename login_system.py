from tkinter import *
import os

def delete1():
    screen1.destroy()

def delete2():
    screen2.destroy()

def delete3():
    screen3.destroy()

def login_success():
    global screen1
    screen1 = Toplevel(homescreen)
    screen1.geometry("100x100")
    Label(screen1,text = "Login success").pack()
    Button(screen1,text = "OK",command = delete1).pack()

def Incorrect_password():
    global screen2
    screen2 = Toplevel(homescreen)
    screen2.geometry("100x100")
    Label(screen2,text = "Password incorrect").pack()
    Button(screen2,text = "OK",command = delete2).pack()

def User_not_found():
    global screen3
    screen3 = Toplevel(homescreen)
    screen3.geometry("100x100")
    Label(screen3,text = "User not found").pack()
    Button(screen3,text = "OK",command = delete3).pack()


def login_conformation():
    username_conformation = username.get()
    password_conformation = password.get()

    username_varify.delete(0,END)
    password_varify.delete(0,END)
    list_of_files = os.listdir()
    if username_conformation in list_of_files:
        file1 = open(username_conformation, "r")
        varify = file1.read().splitlines()
        if password_varify in varify:
            login_success()
        else:
            Incorrect_password()
    else:
        User_not_found()
        

def login_page():
    login = Toplevel(homescreen)
    login.geometry("400x400")
    login.title("Login page")

    global username
    global password
    username = StringVar()
    password = StringVar()

    global username_varify
    global password_varify
    Label(login, text = "Username", width = 20).pack()
    username_varify = Entry(login, textvariable = username)
    username_varify.pack()
    Label(login, text = "").pack()
    Label(login, text = "Password", width = 20).pack()
    password_varify = Entry(login, textvariable = password, show = "*")
    password_varify.pack()
    Label(login, text = "").pack()
    Button(login, text = "Enter", width = 30, font=("Arial",20),command = login_conformation).pack()

def registration_confirm():
    password_detail = Username.get()
    username_detail = Password.get()

    file = open(username_detail, "w")
    file.write(username_detail+"\n")
    file.write(password_detail)
    file.close()
    username_register.delete(0,END)
    password_register.delete(0,END)

    Label(register, text = "Submition success!").pack()    


def registration_page():
    global register
    register = Toplevel(homescreen)
    register.geometry("400x400")
    register.title("Registration page")

    global Username
    global Password

    Username = StringVar()
    Password = StringVar()
    
    global username_register
    global password_register

    Label(register,text = "Username",font=("Arial",20)).pack()
    username_register = Entry(register, textvariable = Username)
    username_register.pack()
    Label(register,text = "").pack()
    Label(register,text = "Password",font=("Arial",20)).pack()
    password_register = Entry(register, textvariable = Password, show = "*")
    password_register.pack()
    Label(register,text = "").pack()
    Button(register, text = "Submit",width = 20, height = 1, command = registration_confirm).pack()

def Home_screen():
    global homescreen
    homescreen = Tk()
    homescreen.geometry("400x400")
    homescreen.title("Login and Register page")
    Button(text = "Login", width = 30, height = 1, bg = "green", font=("Arial",20), command = login_page).pack()
    Button(text = "Register", width = 30, height = 1, bg = "green", font=("Arial",20),command = registration_page).pack()
    homescreen.mainloop()
Home_screen()