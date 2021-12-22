# Function Name :  Pattern()  
#
# Description   :  Write a program which accept one number for user and check whether number is prime or not.
#
# Input         :  Integer
#
# Output        :  Integer
#
# Author        :  Rahul Patil

from typing import Pattern


def Pattern(iValue):
    i = 1
    flag = False

    for i in range(iValue):

        j = i + 1
        
        for k in range(j,iValue+1):
            
            print("*",end=" ")

        print("\n")

def main():

    iNo = int(input("Enter the First Number: "))

    iRet = Pattern(iNo)

    if(iRet == True):
        print("Number is not prime")
    else:
        print("Number is prime")
if __name__ == "__main__":
    main()
