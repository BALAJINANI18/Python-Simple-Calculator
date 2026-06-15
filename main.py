while True:
    
    a = int(input("\nEnter Number 1: "))

    b = int(input("\nEnter Number 2: "))
    
    print("\n1.Addition")
    print("\n2.Subtraction")
    print("\n3.Multiplication")
    print("\n4.Division")
    print("\n5.Exit")
    choice = int(input("\nEnter choice: "))
    if choice==1:
        add = a+b
        
        print("Result: " , add )
        
    elif choice==2:
        sub = a-b;
        
        print("Result: " , sub)
        
    elif choice==3:
        
        multiply = a*b
        
        print("Result: " , multiply)
       
    elif choice==4:
        if b!=0:
            div = a/b
            print("Result: " , div)
        else:
            print("Cannot divide by Zero")
        
        
    elif  choice==5:
        print("Program exiting!")
        break
    else:
        print("Invalid choice")

