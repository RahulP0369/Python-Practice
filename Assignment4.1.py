
# Function Name :  Power()  
#
# Description   :  Write a program which contains one lambda function which accepts one parameter and return 
#                  power of two.
#
# Input         :  Integer
#
# Output        :  Integer
#
# Author        :  Rahul Patil

Power = lambda no1 : no1 ** 2

def main():

    iNo = int(input("Enter Number: "))

    iRet = Power(iNo)
    print(iRet)

if __name__ == '__main__':
    main()