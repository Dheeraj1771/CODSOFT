#Task on creating a To Do List
'''A To-Do List application is a useful project that helps users manage and organize their tasks efficiently.
This project aims to create a command-line or GUI-based application using Python, allowing users to create, update, and track their to-do lists'''
l=[]
#Function to Add Task to the To Do List 
def add():
    inp=input("Enter the Task That you want to add to the To Do List (E.g.: 1. Play Basketball): ")
    l.append(inp)
    print("The Task was added successfully..")

#Function to Delete Task to the To Do List 
def delete():
    print("Here is your To Do List, Which Task would you like to delete?")
    for i in l:
        print(i)
    a=input("Enter the Task that you want to delete: ")
    l.remove(a)
    print("The Task was Deleted Successfully")

#Function to Update Task to the To Do List 
def update():
    print("Here is your To Do List, Which Task would you like to delete?")
    for i in l:
        print(i)
    a=input("Enter the Task that you want to update: ")
    l.remove(a)
    b=input("Enter the New Task that you want to add: ")
    l.append(b)
    print("The Task was updated successfully")   

#Function to Display all Task of the To Do List     
def display():
    print("Your To do List is as follows: ")
    for i in l:
        print(i)
#The Main Menu
while True:
    print("Welcome to the To Do List Menu")
    print("1. Add Task to the To Do List")
    print("2. Delete Task from the To Do List")
    print("3. Update Task from the To Do List")
    print("4. Display Task of the To Do List")
    print("5. Exit the Menu")
    ch=int(input("Enter your desired choice from the following: (E.g.: '1' for first choice): "))
    if ch==1: 
        add()

    elif ch==2:
        if len(l)==0:
            print("The To Do List is Empty, There is no task to Delete.")
        else:
            delete()

    elif ch==3:
        if len(l)==0:
            print("The To Do List is Empty, There is no task to Update.")
        else:
            update()

    elif ch==4:
        if len(l)==0:
            print("You don't have any Task in your To Do List.")
        else:
            display()

    elif ch==5:
        print("Exiting the To Do List Menu....")
        break;

    else:
        print("Enter a Correct Chocie...")

