# Function Name :  SumDigitR()  
#
# Description   :  recursive program which accept number from user and return 
#                  summation of its digits.
#
# Input         :  Integer
#
# Output        :  Integer
#
# Author        :  Rahul Patil

def SumDigitR(x, iSum = 0):
    if x != 0:
        Temp = x%10
        x = int(x/10)
        iSum= iSum+Temp
        return SumDigitR(x,iSum)
        
    return iSum

def main():
    iNo = int(input("Enter Number: "))
    iRet = SumDigitR(iNo)
    print(iRet)

if __name__ == "__main__":
    main()