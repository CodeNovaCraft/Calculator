print("Welcome to Calculator!")

x = input("Do you want to calculate?(y/n) ")
while x=="y":
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    print("Oparation Availabe \n1: for Addition \n2: for Subtraction \n3: for Multiplication \n4:for Divition")

    opt = int(input("What Oparation do you want?(Enter Number)-> "))

    if opt == 1:
        print(f"{num1} + {num2} =", num1+num2)
    elif opt == 2:
        print(f"{num1} - {num2} =", num1-num2)
    elif opt == 3:
        print(f"{num1} * {num2} =", num1*num2)
    elif opt == 4:
        print(f"{num1} / {num2} =", num1/num2)

    print("-"*20,"\n")
    
    x = input("Do you want to calculate again?(y/n) ")

print("Thanks for using Calculator! \nExited")