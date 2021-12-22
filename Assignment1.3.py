# Function Name :  Add()  
#
# Description   :   Write a program which contains one function named as Add() which accepts two numbers 
#                   from user and return addition of that two numbers.
#
# Input         :  Integer
#
# Output        :  Integer
#
# Author        :  Rahul Patil

def Add(iNo1, iNo2):

    return iNo1 + iNo2;

def main():

    iValue = int(input("please Enter the number: "))

    iValue2 = int(input("Please Enter second number: "))

    iRet = Add(iValue, iValue2)

    print("Addition of both number is: ",iRet)

if __name__ == "__main__":
    main()
