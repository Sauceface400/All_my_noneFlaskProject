import tkinter
import random
"""
root = tkinter.Tk()

root.configure(bg="white")

root.title("my list")

root.geometry("225x230")

#create an empty list
tasks = []

tasks = ["kick","eat","pee"]

#this will insert the task below the task instead of above
def update():
    clear_lb()
    for task in tasks:
        lb_list.insert("end", task)

def clear_lb():
    lb_list.delete(0,"end")

#thi will get the value of the txt box
def add_task():
    task = txt_input.get()
    #if the task != "" it will add into the list of tasks
    if task != "":
        tasks.append(task)
        update()
    else:
        #if the task = "" then this will pop-up(a value is not enter in the textbox)
        lbl_display["text"]="pls enter something"
    txt_input(0, "end")

def clear():
    global tasks

    tasks = []
    update()

def delete():
    task = lb_list.get("active")
    if task in tasks:
        #this will remove of the task within the list-box
        tasks.remove(task)
    update()

def asc_btn():
    tasks.sort()
    update()

def desc_btn():
    tasks.sort()
    tasks.reverse()
    update()

def random_btn():
    task = random.choice(tasks)
    lbl_display["text"] = task

def num_task():
    number_of_tasks = len(tasks)
    #will display the number of task that is inside the listbox 
    msg = "the num of task: %s" %number_of_tasks
    lbl_display["text"] = msg

def exit_btn():
    pass

lbl_title = tkinter.Label(root, text="to do list", bg="white")
lbl_title.grid(row=0,column=0)

lbl_display = tkinter.Label(root, text="", bg="white")
lbl_display.grid(row=0,column=1)

txt_input = tkinter.Entry(root, width=20)
txt_input.grid(row=1,column=1)

btn_add_task = tkinter.Button(root, text="add task",width=10, command=add_task)
btn_add_task.grid(row=1,column=0)

delete_all = tkinter.Button(root, text="delete all",width=10, command=clear)
delete_all.grid(row=2,column=0)

delete_one = tkinter.Button(root, text="delete",width=10, command=delete)
delete_one.grid(row=3,column=0)

asc = tkinter.Button(root, text="asc",width=10, command=asc_btn)
asc.grid(row=4,column=0)

desc = tkinter.Button(root, text="desc",width=10, command=desc_btn)
desc.grid(row=5,column=0)

random_task = tkinter.Button(root, text="random",width=10, command=random_btn)
random_task.grid(row=6,column=0)

task_number = tkinter.Button(root, text="task number",width=10, command=num_task)
task_number.grid(row=7,column=0)

btn_exit = tkinter.Button(root, text="exit",width=10, command=exit_btn)
btn_exit.grid(row=8,column=0)

lb_list = tkinter.Listbox(root)
lb_list.grid(row=2,column=1, rows=7)

root.mainloop()
"""

root = tkinter.Tk()
root.geometry("200x300")
#an empty list
activities = []
#function's
def update():
    delete_f()
    l_input.delete(0, "end")
    for task in activities:
        lb_list.insert("end", task)
def delete_f():
    lb_list.delete(0,"end")
def add():
    task = l_input.get()
    if task != "":
        activities.append(task)
        update()
    else:
        lbl_display["text"]="Enter pls"
    l_input(0,"end")
#label
lbl_display = tkinter.Label(root, text="", bg="white")
lbl_display.pack()
#Add and delete Button
btn_add = tkinter.Button(root, text="Add", width=12, command=add)
btn_add.pack()
btn_delete = tkinter.Button(root, text="Delete", width=12, command=delete_f)
btn_delete.pack()
#the input text and listbox
l_input = tkinter.Entry(root, width=20)
l_input.pack()
lb_list = tkinter.Listbox(root)
lb_list.pack()


root.mainloop()