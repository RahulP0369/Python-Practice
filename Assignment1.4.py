# Function Name :  Pattern()  
#
# Description   :   Write a program which display 5 times Marvellous on screen.
#
# Input         :  integer
#
# Output        :  string
#
# Author        :  Rahul Patil

def Pattern(iNo):

    for i in range(iNo):
        print("Marvellous")

def main():

    iValue = int(input("please Enter the number: "))

    iRet = Pattern(iValue)

if __name__ == "__main__":
    main()
