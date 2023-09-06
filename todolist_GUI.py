from tkinter import *

root = Tk()
root.minsize(400, 200)
root.maxsize(400, 200)


# Functions of Buttons
def add_task_button():
    with open('file.txt', 'a') as addtask:
        addtask.write(f"{add_task_entry.get()}\n")
        print(f"{add_task_entry.get()} added to task list")


def complete_task_button():
    try:
        with open('file.txt', 'r') as completetask:
            list_item = completetask.readlines()
            list_item = list(
                map(lambda x: x.replace(f'{complete_task_entry.get()}', f'{complete_task_entry.get()}-This task '
                                                                        f'is completed'), list_item))
            file = open('file.txt', 'w')
            file.writelines(list_item)
            file.close()
    except:
        print("This task is not Present on your doing list")


def delete_task_button():
    try:
        with open('file.txt', 'r') as deletetask:
            dlt_item = deletetask.readlines()
            dlt_item.remove(f"{delete_task_entry.get()}\n")
            with open('file.txt', 'w') as newlist:
                for item in dlt_item:
                    newlist.write(item)
    except:
        print("This task is not available or already completed")


def view_task_button():
    with open('file.txt', 'r') as view:
        print(view.read())


def exit_button():
    print("Exitting", end=" ")
    print(".", end=" ")
    time.sleep(0.5)
    print(".", end=" ")
    time.sleep(0.5)
    print(".", end=" ")
    time.sleep(0.5)
    print(".", end=" ")
    time.sleep(0.5)
    print(".", end=" ")
    time.sleep(0.5)
    print(".", end=" ")
    time.sleep(0.5)
    exit()


# Labels
add_task = Label(root, text="1. Add Task")
complete_task = Label(root, text="2. Mark as Completed")
delete_task = Label(root, text="3. Delete Task")

# Pack Labels
add_task.grid(row=1, column=1)
complete_task.grid(row=2, column=1)
delete_task.grid(row=3, column=1)

# Set Variables
addtaskvalue = StringVar()
completetaskvalue = StringVar()
deletetaskvalue = StringVar()

# Entry / Input
add_task_entry = Entry(root, textvariable=addtaskvalue)
complete_task_entry = Entry(root, textvariable=completetaskvalue)
delete_task_entry = Entry(root, textvariable=deletetaskvalue)

# Pack Entries / Inputs
add_task_entry.grid(row=1, column=2)
complete_task_entry.grid(row=2, column=2)
delete_task_entry.grid(row=3, column=2)

# Buttons
b1 = Button(text="Add Your Task", command=add_task_button)
b2 = Button(text="Task Completed", command=complete_task_button)
b3 = Button(text="Delete", command=delete_task_button)
b4 = Button(text="View Tasks", command=view_task_button)
b5 = Button(text="Exit", command=exit_button)

# Pack Buttons
b1.grid(row=1, column=3)
b2.grid(row=2, column=3)
b3.grid(row=3, column=3)
b4.grid(row=4, column=2)
b5.grid(row=5, column=2)

root.mainloop()
