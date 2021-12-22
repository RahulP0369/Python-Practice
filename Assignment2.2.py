# Function Name :  PrientEvenNumbers()  
#
# Description   :  Write a program which accept one number and display below pattern.
#
# Input         :  Integer
#
# Output        :  string
#
# Author        :  Rahul Patil

def Pattern(iValue):
    for i in range(iValue):
        for j in range(iValue):
            print("*",end=" ")
        print("\n")

def main():

    iNo = int(input("Enter the First Number: "))

    iRet = Pattern(iNo)

if __name__ == "__main__":
    main()
