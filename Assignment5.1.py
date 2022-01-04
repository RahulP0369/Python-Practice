
class Demo:

    value = 30;

    def __init__(self,a,b):
        self.iNo1 = a
        self.iNo2 = b
    
    def fun(self):
        print(self.iNo1)
        print(self.iNo2)
    
    def gun(self):
        print(self.iNo1)
        print(self.iNo2)

def main():

    no1 = int(input("Enter first number for obj1: "))
    no2 = int(input("Enter second number for obj1: "))

    no3 = int(input("Enter first number for obj2: "))
    no4 = int(input("Enter second number for obj2: "))

    obj1 = Demo(no1,no2)
    obj1.fun()
    obj1.gun()

    obj2 = Demo(no3, no4)
    obj2.fun()
    obj2.gun()
    
if __name__ == "__main__":
    main()