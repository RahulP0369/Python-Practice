# Function Name :  main()  
#
# Description   :  Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub() 
#                  for subtraction, Mult() for multiplication and Div() for division. All functions accepts two 
#                  parameters as number and perform the operation. Write on python program which call all the 
#                  functions from Arithmetic module by accepting the parameters from user.
#
# Input         :  Integer
#
# Output        :  Integer
#
# Author        :  Rahul Patil

import Assignment2X1Package as Arithmatics

def main():

    iNo = int(input("Enter the First Number: "))
    iNo2 = int(input("Enter the Second Number: "))

    print("Addition is=",Arithmatics.Add(iNo,iNo2))
    print("Substraction is=",Arithmatics.Sub(iNo,iNo2))
    print("Multiplication is=",Arithmatics.Mul(iNo,iNo2))
    print("Devision is=",Arithmatics.Div(iNo,iNo2))

if __name__ == "__main__":
    main()
