
class BankAccount:

    ROI = 10.5

    def __init__(self,a,b):
        self.Name = a
        self.Amount = b
    
    def Deposit(self,deposit):
        self.Amount = self.Amount + deposit
    
    def Withdrawl(self,deposit):
        self.Amount = self.Amount - deposit

    def CalculateInterest(self,T):
        SI = (self.Amount * BankAccount.ROI * T) / 100
        print("Simple Interest is: ",SI)

    def Display(self):
        print("Name of holder is: ",self.Name)
        print("Amount of holder is: ",self.Amount)

def main():
    obj1 = BankAccount("rohan",5000)
    obj1.Display()

    obj1.Deposit(5000)
    obj1.Display()

    obj1.Withdrawl(2000)
    obj1.Display()

    obj1.CalculateInterest(3)

if __name__ == "__main__":
    main()