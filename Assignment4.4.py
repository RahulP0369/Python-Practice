# Function Name :  DataFilter(), CalculateSquare(), Addition()  
#
# Description   :  Write a program which contains filter(), map() and reduce() in it. Python application which 
#                  contains one list of numbers. List contains the numbers which are accepted from user. Filter 
#                  should filter out all such numbers which are even. Map function will calculate its square. 
#                  Reduce will return addition of all that numbers.
#
# Input         :  Integer
#
# Output        :  Integer
#
# Author        :  Rahul Patil

from functools import reduce

DataFilter = lambda iNo : (iNo % 2 == 0)

CalculateSquare = lambda iNo : iNo ** 2

Addition = lambda iNo1, iNo2 : iNo1 + iNo2

def main():

    iValues = int(input("Enter size of list: "))
    list1 = []

    for i in range(iValues):
        element = int(input("Enter the element: "))
        list1.append(element)

    print("Input List = ",list1)

    FilteredData = list(filter(DataFilter, list1))
    print("List after filter = ",FilteredData)

    Square = list(map(CalculateSquare, FilteredData))
    print("List after map = ",Square)

    AdditionOfSquare = reduce(Addition, Square)
    print("Output of reduce = ",AdditionOfSquare)    


if __name__ == "__main__":
    main()