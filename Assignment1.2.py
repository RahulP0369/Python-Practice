# Function Name :  ChkNum()  
#
# Description   :   Write a program which contains one function named as ChkNum() which accept one 
#                   parameter as number. If number is even then it should display “Even number” otherwise 
#                   display “Odd number” on console.
#
# Input         :  integer
#
# Output        :  string
#
# Author        :  Rahul Patil

def ChkNum(iNo):

    bRet = False;

    if(iNo % 2 == 0):
        return True;
    
    else:
        return False;

def main():

    iValue = int(input("please Enter the number"))

    iRet = ChkNum(iValue)

    if(iRet == True):
        print("Number is even");
    
    else:
        print("Number is odd");

if __name__ == "__main__":
    main()
