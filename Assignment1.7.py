# Function Name :  ChkNum()  
#
# Description   :  Write a program which contains one function that accept one number from user and returns 
#                  true if number is divisible by 5 otherwise return false.
#
# Input         :  integer
#
# Output        :  string
#
# Author        :  Rahul Patil

def Divisible(iNo):

    if((iNo % 5) == 0):

        return True

    else:
        return False

def main():

    iValue = int(input("please Enter the number: "))

    iRet = Divisible(iValue)

    if(iRet == True):
    
        print("Number is divisible by 5")
    
    else:
        print("Number is not divisible by 5")

if __name__ == "__main__":
    main()
