# Function Name :  Prime()  
#
# Description   :  Write a program which accept one number for user and check whether number is prime or not.
#
# Input         :  Integer
#
# Output        :  Integer
#
# Author        :  Rahul Patil

def Prime(iValue):
    i = 1
    flag = False

    while iValue > i:
        if iValue % 2 == 0:
            flag = True
        i = i+1

    return flag

def main():

    iNo = int(input("Enter the First Number: "))

    iRet = Prime(iNo)

    if(iRet == True):
        print("Number is not prime")
    else:
        print("Number is prime")
if __name__ == "__main__":
    main()
