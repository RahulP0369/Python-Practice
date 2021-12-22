# Function Name :  FactAdd()  
#
# Description   :  Write a program which accept one number form user and return addition of its factors.
#
# Input         :  Integer
#
# Output        :  Integer
#
# Author        :  Rahul Patil

def FactAdd(iValue):
    i = 1
    sum = 0

    while iValue > i:
        if iValue % i == 0:
            sum = sum + i
        i = i+1

    return sum

def main():

    iNo = int(input("Enter the First Number: "))

    iRet = FactAdd(iNo)

    print(iRet)
if __name__ == "__main__":
    main()
