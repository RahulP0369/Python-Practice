# Function Name :  Pattern()  
#
# Description   :   Write a program which accept number from user and print that number of “*” on screen.
#
# Input         :  integer
#
# Output        :  string
#
# Author        :  Rahul Patil

def Pattern(iNo):

    for i in range(iNo):
        print("*",end=" ")

def main():

    iValue = int(input("please Enter the number: "))

    iRet = Pattern(iValue)

if __name__ == "__main__":
    main()
