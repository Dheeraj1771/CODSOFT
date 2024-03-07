#Simple Calculator
#Welcome Note
print("Welcome to the Simple Calculator")
print("Here the user can perform basic arithmetic operations by inputting two numbers of their choice.")

#Asking User to Input the Two Numbers 
while True:
    a=int(input("Enter the First Number: "))
    b=int(input("Enter the Second Number: "))
    ch=input('''Enter the opperation that you want to perform on the two numbers
For E.g.:'+' : Addition
         '-' : Substartion
         '*' : Multiplication
         '/' : Division
Please Enter your Choice here: ''')
    #Addition Operation 
    if ch=="+":
        c=a+b
        print("The Addition of Two Numbers is: ",c)

    #Substraction Operator 
    elif ch=="-":
        c=a-b
        print("The Substration of Two Numbers is: ",c)

    #Multiplication Operator 
    elif ch=="*":
        c=a*b
        print("The Product of Two Numbers is: ",c)

    #Division Operator 
    elif ch=="/":
        c=a/b
        print("The Divison of Two Numbers is: ",c)

    else:
        print("Enter the correct choice...")

    #Asking user if thy want to proceed ahead 
    chh=input("Do you want to continue ('Yes' or 'No'): ")
    if chh=="Yes":
        continue
    elif chh=="No":
        print("Exiting the calculator...")
        break
    else:
        print("Enter the correct choice...")
