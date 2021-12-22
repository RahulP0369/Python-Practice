# Function Name :  PrientEvenNumbers()  
#
# Description   :  Write a program which display first 10 even numbers on screen.
#
# Input         :  Integer
#
# Output        :  Integer
#
# Author        :  Rahul Patil

def PrintEvenNumbers(iNo):

    iNo = iNo+1

    for i in range(1,iNo*2):
        if((i % 2) == 0):
            print(i,end=" ")

def main():

    iValue = int(input("please Enter the number: "))

    iRet = PrintEvenNumbers(iValue)

if __name__ == "__main__":
    main()
