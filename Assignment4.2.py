# Function Name :  Multi()  
#
# Description   :  Write a program which contains one lambda function which accepts two parameters and return 
#                  its multiplication.
#
# Input         :  Integer
#
# Output        :  Integer
#
# Author        :  Rahul Patil


from typing import MutableMapping


Multi = lambda iNo1, iNo2 : iNo1 * iNo2

def main():

    iValue1 = int(input("Enter first number: "))
    iValue2 = int(input("Enter second number: "))

    iRet = Multi(iValue1, iValue2)
    print(iRet)

if __name__ == "__main__":
    main()
