# Function Name :  ChkNumber()  
#
# Description   :   Write a program which accept number from user and check whether that number is positive or 
#                   negative or zero.
#
# Input         :  integer
#
# Output        :  string
#
# Author        :  Rahul Patil

def ChkNumber(iNo): 

    if iNo > 0: 
        print("Number is positive")
    
    elif iNo < 0:
        print("Number is negative")

    elif iNo == 0:
        print("Number is zero")
    

def main():

    iValue = int(input("please Enter the number: "))

    iRet = ChkNumber(iValue)

if __name__ == "__main__":
    main()
