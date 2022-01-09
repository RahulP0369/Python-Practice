# Function Name :  DisplayR()  
#
# Description   :  A recursive program which display below pattern
#
# Input         :  Integer
#
# Output        :  char
#
# Author        :  Rahul Patil

def DisplayR(iValue):
    
    if(iValue > 0):
        print("*",end=" ")
        iValue = iValue-1
        DisplayR(iValue)


def main():

    iNo = int(input("Enter Number: "))
    DisplayR(iNo)

if __name__ == "__main__":
    main()