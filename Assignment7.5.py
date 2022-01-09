# Function Name :  FactR()  
#
# Description   :  recursive program which accept number from user and return its 
#                  factorial.
#
# Input         :  Integer
#
# Output        :  Integer
#
# Author        :  Rahul Patil

def FactR(iValue, iFact = 1):

    if (iValue != 0):

        iFact = iFact * iValue
        iValue = iValue-1
        return FactR(iValue,iFact)
    return iFact

def main():
    iNo = int(input("Enter Number: "))
    iRet = FactR(iNo)
    print(iRet)

if __name__ == "__main__":
    main()