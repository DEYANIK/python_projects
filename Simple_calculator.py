print("~~~~~~ WELCOME TO CALCULATOR ~~~~~~")
num1 = float(input("enter your first number:"))
num2 = float(input(" enter your second number:"))
print ("please choose your operations: \n press 1 for addition \n press 2 for substraction \n press 3 for multiplication \n press 4 for division")
choice = int(input("choose your operation: "))
if choice == 1:
    print("The addition result is: ",num1+num2)
elif choice == 2:
    print("The substraction result is: ",num1-num2)
elif choice == 3:
    print("The multiplication result is: ",num1*num2)
elif choice == 4:
    if num2 !=0 :
        print("The division result is: ",num1/num2)
    else: print("Invalid input")

else: print("invalid input, please try again")
print ("Thank-you for using my calculator, hope you have a nice day.")
