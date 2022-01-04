
class Arithmatic:

    PI = 3.14

    def __init__(self):
        self.iNo1 = 0
        self.iNo2 = 0
    
    def Accept(self):
        print("Enter First No: ")
        self.iNo1 = int(input())

        print("Enter Second No: ")
        self.iNo2 = int(input())

    def Addition(self):
        return self.iNo1+self.iNo2
    
    def Sub(self):
        return self.iNo1 - self.iNo2

    def MultiPlication(self):
        return self.iNo1 * self.iNo2

    def division(self):
        return self.iNo1 / self.iNo2

def main():

    obj1 = Arithmatic()

    obj1.Accept()
    iRetAdd = obj1.Addition()
    iRetSub = obj1.Sub()
    iRetMul = obj1.MultiPlication()
    iRetDiv = obj1.division()

    obj2 = Arithmatic()

    obj2.Accept()
    iRetAdd2 = obj2.Addition()
    iRetSub2 = obj2.Sub()
    iRetMul2 = obj2.MultiPlication()
    iRetDiv2 = obj2.division()

    print("Addition is:\n",iRetAdd,"\nSubstractions is:\n",iRetSub,"\nMultiplication is:\n",iRetMul,"\nDivision is:\n",iRetDiv)
    print("Addition is:\n",iRetAdd2,"\nSubstractions is:\n",iRetSub2,"\nMultiplication is:\n",iRetMul2,"\nDivision is:\n",iRetDiv2)

if __name__ == "__main__":
    main()