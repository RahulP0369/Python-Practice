
class Arithmatic:
    
    def __init__(self,a):
        self.Value = a
    
    def ChkPrime(self):
        no = self.Value
        i = 2
        if(no <= i):
            return False

        while no > i:
            if no % 2 == 0:
                flag = False
    
            else:
                flag = True

            i = i+1

        return flag

    def ChkPerfect(self):
        no = self.Value
        iSum = 0
        for i in range(1,no):
            if((no % i) == 0):
                iSum = iSum + i
        
        if(iSum == no):
            return True
        else:
            return False        

    def SumFactors(self):
        no = self.Value
        iSum = 0
        for i in range(1,no):
            if((no % i) == 0):
                iSum = iSum + i

        return iSum

    def Factors(self):
        no = self.Value
        arr = []

        for i in range(1, no):
            if ((no % i) == 0):
                arr.append(i)
        return arr
    
def main():
    iValue = int(input("Enter Number: "))
    arr = []

    obj1 = Arithmatic(iValue)
    
    print("Number is Prime: ",obj1.ChkPrime())
    print("Entered Number is perfect (True or Fale): ",obj1.ChkPerfect())
    arr = obj1.Factors()
    print(arr)

    iValue1 = int(input("Enter Number: "))
    obj2 = Arithmatic(iValue1)

    print("Number is prime: ",obj2.ChkPrime())
    print("Entered Number is perfect (True or False): ",obj2.ChkPerfect())
    arr = obj2.Factors()
    print(arr)

if __name__ == "__main__":
    main()
