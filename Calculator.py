import math
import numpy


def calculation(choice,num1,num2):
    match (choice):
        case 1:
            result=numpy.add(num1,num2)
            print(f"{num1}+{num2}={result}")    
        case 2:
            result=numpy.subtract(num1,num2)
            print(f"{num1}-{num2}={result}")
        case 3:
            try:
                #result=numpy.divide(num1,num2)
                result=num1/num2
                print(f"{num1}%{num2}={result}")
            except ZeroDivisionError as e:
                print("Error You have divide by 0 !! Invalid",e)

        case 4:
            result=numpy.multiply(num1,num2)
            print(f"{num1}*{num2}={result}")
        case 5:
            result=numpy.power(num1,num2)
            print(f"{num1}**{num2}={result}")
        case 6:
            result=math.sqrt(num1)
            print(f"root of {num1}={result}")
        case default:
            print("Invalid Input by the user..")


print("Welcome !! Enter any choice for below operation:-")
print("1.Addition 2.Subtraction 3.Division 4.Multiplication 5.Power 6.Root")
choice=int(input("Enter the choice between 1-6 :-\n"))
num1=int(input("Enter first Number :-"))
num2=int(input("Enter second Number :-"))
calculation(choice,num1,num2)
