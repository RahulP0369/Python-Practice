# Function Name :  FilterNumber(), Increment(), Product()  
#
# Description   :  Write a program which contains filter(), map() and reduce() in it. Python application which 
#                  contains one list of numbers. List contains the numbers which are accepted from user. Filter 
#                  should filter out all such numbers which greater than or equal to 70 and less than or equal to 
#                  90. Map function will increase each number by 10. Reduce will return product of all that 
#                  numbers.
#
# Input         :  Integer
#
# Output        :  Integer
#
# Author        :  Rahul Patil

from functools import reduce

FilterNumber = lambda iNo : (iNo >= 70 and iNo <= 90)

Increment  = lambda iNo : iNo + 10

Product = lambda iNo1,iNo2 : iNo1 * iNo2

def main():

    iValues = int(input("Enter size of list: "))
    list1 = []

    for i in range(iValues):
        element = int(input("Enter the element: "))
        list1.append(element)

    print("Original Data: ",list1)

    filterdata = list(filter(FilterNumber,list1))

    print("Data after filter: ",filterdata)

    incrementdata  = list(map(Increment,filterdata))

    print("Data after incremented by no: ",incrementdata)
    
    productOfNo = reduce(Product, incrementdata)

    print("Product after filter and map: ",productOfNo)


if __name__=='__main__':
    main()