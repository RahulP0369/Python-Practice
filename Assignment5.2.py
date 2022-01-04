
class Circle:

    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Cirf = 0.0
    
    def Accept(self):
        print("Enter Value For Radius: ")
        self.Radius = float(input())

    def CalculateArea(self):
        self.Area = self.PI * self.Radius ** 2
    
    def CalculateCircumference(self):
        self.Cirf = self.Radius*2

    def Display(self):
        print("Area is: ",self.Area)
        print("Circumference is: ",self.Radius)

def main():

    obj1 = Circle()
    obj2 = Circle()

    obj1.Accept()
    obj1.CalculateArea()
    obj1.CalculateCircumference()
    obj1.Display()

    obj2.Accept()
    obj2.CalculateArea()
    obj2.CalculateCircumference()
    obj2.Display()
    
if __name__ == "__main__":
    main()