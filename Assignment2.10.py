# Function Name :  PrientEvenNumbers()  
#
# Description   :  Write a program which display first 10 even numbers on screen.
#
# Input         :  Integer
#
# Output        :  Integer
#
# Author        :  Rahul Patil


def Digit(iNo):

    i = 0
    iCnt = 0
    while(iNo != 0):
        i = iNo % 10

        iCnt = iCnt + i;

        iNo = iNo // 10

    return iCnt


def main():

    iValue = int(input("please Enter the number: "))

    iRet = Digit(iValue)

    print(iRet)
if __name__ == "__main__":
    main()
