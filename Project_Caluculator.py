while(True):
    print("Select a Operator :")
    print("1. ADDITION")
    print("2. SUBTRACTION")
    print("3. MULTIPLICATION")
    print("4. DIVISION")
    print("5. SQ ROOT")

    selected_Operator = input("Enter Your Choice Operator(1/2/3/4/5)")
    if selected_Operator in ("1","2","3","4"):
        num1 =float(input("Enter Your Frist Number: "))
        num2 =float(input("Enter Your Second Number: "))

        if selected_Operator == "1" :
            print(num1 , "+" , num2 ,"=",num1+num2)
        elif selected_Operator == "2" :
            print(num1 , "-" , num2 ,"=",num1-num2)
        elif selected_Operator == "3" :
            print(num1 , "X" , num2 ,"=",num1*num2)
        elif selected_Operator == "4" :
            print(num1 , "/" , num2 ,"=",num1/num2)
    elif selected_Operator == "5":
        num1 =float(input("Enter Your Number: "))
        num2 =float(input("Enter Your Power : "))
        print(num1 , "**" , num2 ,"=",num1**num2)
        

    else:
        print("Invalid Choice Operator,Enter a Valid Operator")
    
    END = input("Want one more Calculation(Yes/No): ")
    if END == "No":
        break
    elif END == "Yes" :
        continue
    else:
        print("invalid")
        break




