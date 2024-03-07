#Code for Contact Book.

#Function to Add Contact Details to the Contact Book 
def add():
    sr=int(input("Enter the Serial Number: "))
    name=input("Ente the Name of the Person: ")
    ph=input("Enter the Phone Number of the Person: ")
    em=input("Enter the E-mail of the Person: ")
    ad=input("Enter the Address of the Person: ")
    a=[sr,name,ph,em,ad]
    l.append(a)
    print("The Conact Details are saved successfully!!")

#Function to View the Contact Details in the Contact Book 
def view():
    print("The Contact Information is as follows: ")
    for i in l:
        print(i)

#Function to search Contact Details in the Contact Book
#By Name       
def search1():
    a=input("Enter the Name by which you want to search the Contact Information: ")
    flag=0
    for i in l:
        if i[1]==a:
            flag=1
            print("The Search for the Name,",a,"was successful!!")
            print("Here is the Contact Infomation")
            print(i)
    if flag==0:
        print("There was no such Name as",a,"in the Contact Book")
            
#By Phone Number        
def search2():
    a=input("Enter the Phone Number by which you want to search the Contact Information: ")
    flag=0
    for i in l:
        if i[2]==a:
            flag=1
            print("The Search for the Phone Number,",a,"was successful!!")
            print("Here is the Contact Infomation")
            print(i)
    if flag==0:
        print("There was no such Phone Number as",a,"in the Contact Book")

#Function to Update The Contact Details in the Contact Book             
def update():
    a=input("Enter the Name for which you want to update the Contact Information: ")
    flag=0
    for i in l:
        if i[1]==a:
            flag=1
            l.remove(i)
            sr=int(input("Enter the New Serial Number: "))
            name=input("Ente the New Name of the Person: ")
            ph=input("Enter the New Phone Number of the Person: ")
            em=input("Enter the New E-mail of the Person: ")
            ad=input("Enter the New Address of the Person: ")
            b=[sr,name,ph,em,ad]
            l.append(b)
            print("The Contact Information was Updated Successfully!!")
            
    if flag==0:
        print("There was no such Name as",a,"in the Contact Book")
        print("The Update was not Successful")

#Function to Delete Contact Details in the Contact Book 
def delete():
    a=input("Enter the Name for which you want to Delete the Contact Information: ")
    flag=0
    for i in l:
        if i[1]==a:
            flag=1
            l.remove(i)
            print("The Contact Information was deleted Successfully!!")
    if flag==0:
        print("There was no such Name as",a,"in the Contact Book")
        print("The Update was not Successful")
    

l=[]
#Main Menu 
while True:
    print("Welcome to the Contact Book Menu")
    print("Here you can Add, View, Search, Update, and Delete the contact information as per your needs.") 
    print("1. Add Contact Information")
    print("2. View the Contact Information")
    print("3. Search the Contact Information")
    print("4. Update the Contact Information")
    print("5. Delete the Contact Information")
    print("6. Exit the Menu")
    ch=int(input("Enter your choice (For E.g. '1' for the first choice): "))

    if ch==1:
        add()

    elif ch==2:
        if len(l)==0:
            print("The Contact Book is empty, There is nothing to view!!")
        else:
            view()

    elif ch==3:
        if len(l)==0:
            print("The Contact Book is empty, There is nothing to Search!!")
        else:
            print("You can Search the Contact Information using two Methods: ")
            print("1. By Name")
            print("2. By Phone Number")
            ch=int(input("Enter your Choice for Searching the Contact Information (For E.g. '1' for the first choice): "))
            if ch==1:
                search1()
            elif ch==2:
                search2()
            else:
                print("Please Enter the Correct Choice...")
                
    elif ch==4:
        if len(l)==0:
            print("The Contact Book is empty, There is nothing to Update!!")
        else:
            update()

    elif ch==5:
        if len(l)==0:
            print("The Contact Book is empty, There is nothing to Delete!!")
        else:
            delete()

    elif ch==6:
        print("Exiting the Contact Information Menu....")
        break

    else:
        print("Please Enter the Correct Choice...")
        


    
    
