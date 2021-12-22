# Function Name :  Number()  
#
# Description   :   Write a program which display 10 to 1 on screen
#
# Input         :  Integer
#
# Output        :  Integer
#
# Author        :  Rahul Patil

def Number(iNo):

    while iNo > 0:
        print(iNo,end=" ")
        iNo= iNo-1;

def main():

    iValue = int(input("please Enter the number: "))

    iRet = Number(iValue)

if __name__ == "__main__":
    main()
