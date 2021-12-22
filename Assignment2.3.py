# Function Name :  Factorial()  
#
# Description   :  Write a program which accept one number from user and return its factorial.
#
# Input         :  Integer
#
# Output        :  Integer
#
# Author        :  Rahul Patil

def Factorial(iValue):
    fact = 1

    for i in range (1,iValue+1):
       fact = fact * i 
    return fact

def main():

    iNo = int(input("Enter the First Number: "))

    iRet = Factorial(iNo)

    print(iRet)
if __name__ == "__main__":
    main()
