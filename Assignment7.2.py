# Function Name :  DisplayR()  
#
# Description   :  A recursive program which display below pattern
#
# Input         :  Integer
#
# Output        :  Integer
#
# Author        :  Rahul Patil

def DisplayR(iValue, i =1):
    
    if(iValue > 0):
        print(i,end=" ")
        i = i+1
        iValue = iValue-1
        DisplayR(iValue,i)


def main():

    iNo = int(input("Enter Number: "))
    DisplayR(iNo)

if __name__ == "__main__":
    main()