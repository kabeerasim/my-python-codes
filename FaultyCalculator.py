First = int(input("Enter First Number:\n"))
Operator = str(input("Enter Operator\n"))
Second = int(input("Enter Second number\n"))

Plus = "+"
Minus = "-"
Multiply = "*"
Divide = "/"

if First == 45 and Operator == Multiply and Second == 3:
    print("555")
elif  First == 56 and Operator == Plus and Second == 9:
    print("77")
elif  First == 56 and Operator == Divide and Second == 6:
    print("4")
elif Operator == Plus:
    print(First + Second)
elif Operator == Minus:
    print(First - Second)
elif Operator == Multiply:
    print(First * Second)
elif Operator == Divide:
    print(First / Second)
else: 
    print("Invalid Input!")