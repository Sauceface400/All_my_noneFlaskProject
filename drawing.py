#======Store data============
from tkinter import *
import os

def get_data():
    with open("Storing_information","a") as F:
        inf = dataentered.get()
        F.write(inf + "\n")
    storing.delete(0,END)

def data_page():
    global data
    data = Toplevel(front_page)
    data.geometry("300x250")
    
    Label(data,text="Please enter the data that you want to save",font=("Halvetica",11)).pack()
    
    global dataentered
    dataentered = StringVar()

    global storing
    storing = Entry(data,textvariable=dataentered)
    storing.pack()
    Label(data,text="", height=1).pack()
    Button(data,text="Save", width=5, height=1, font=("Arial",18),command = get_data).pack()

def login_confirmation():
    userscon = personUsername.get()
    passcon = usersPassword.get()
    listfile = os.listdir()
    users.delete(0,END)
    Pass.delete(0,END)

    if  userscon in listfile:
        registration_file = open(userscon, "r")
        varify = registration_file.read().splitlines()
        if passcon in varify:
            data_page()
        else:
            Label(login,text="Incorrect password").pack()
    else:
        Label(login,text="User not found").pack()

def storing_registration():
    users_registration_of_username = Username.get()
    users_registration_of_password = Password.get()

    if len(users_registration_of_password) > 16:
        Label(registration,text="Password cannot exceed more than 16 chracters").pack()
    else:
        file = open(users_registration_of_username,"w")
        file.write(users_registration_of_username + "\n")
        file.write(users_registration_of_password)
        file.close()

        entUse.delete(0, END)
        entPass.delete(0, END)
        Label(registration,text="Registration succesful").pack()

def login_page():
    global login
    login = Toplevel(front_page)
    login.geometry("300x250")
    
    global personUsername
    global usersPassword

    personUsername = StringVar()
    usersPassword = StringVar()

    Label(login ,text="Please login your Username and password").pack
    Label(login ,text="",height=1).pack()

    global users
    Label(login ,text="Username").pack()
    users = Entry(login, textvariable = personUsername)
    users.pack()
    Label(login ,text="").pack()

    global Pass 
    Label(login ,text="Password").pack()
    Pass = Entry(login, textvariable = usersPassword, show="*")
    Pass.pack()
    
    Label(login ,text="").pack()
    Button(login ,text="Login", width=10, height=1, font=("Halvetica",18),command=login_confirmation).pack()

def registration_page():
    global registration
    registration = Toplevel(front_page)
    registration.geometry("300x250")
    
    global Username
    global Password
    Username = StringVar()
    Password = StringVar()

    Label(registration ,text="Please register your Username and password").pack
    Label(registration ,text="",height=1).pack()
    
    Radiobutton()
    Radiobutton()

    global entUse
    Label(registration ,text="Username").pack()
    entUse = Entry(registration, textvariable = Username)
    entUse.pack()
    Label(registration ,text="").pack()

    global entPass
    Label(registration ,text="Password").pack()
    entPass = Entry(registration, textvariable = Password, show="*")
    entPass.pack()
    
    Label(registration ,text="").pack()
    Button(registration ,text="Submit", width=10, height=1, font=("Halvetica",18), command=storing_registration).pack()

def login_and_registration_page():
    global front_page
    front_page = Tk()
    front_page.geometry("500x250")
    front_page.title("TerraSave")
    Label(text="Welcome to our page",font=("Halvetica", 25, "bold")).pack()
    Label(text="",height=1).pack()
    Button(text="Login", height=1, width=10, font=("Arial",18), command=login_page).pack()
    Label(text="",height=1).pack()
    Button(text="Register", height=1, width=10, font=("Arial",18),command=registration_page).pack()
    front_page.mainloop()

login_and_registration_page()