import threading

def EvenFact(iValue):
    iSum = 0
    for i in range(1,iValue):
        if ((iValue % i) == 0):
            iSum = iSum + i
    print("Sum of an Even Factor is: ",iSum)

def OddFact(iValue):
    iSum = 0
    for i in range(1, iValue):
        if((iValue % i) != 0):
            iSum = iSum + i
    print("Sum of an Odd Factor is: ",iSum)

def main():

    iNo = int(input("Enter Number: "))

    thread1 = threading.Thread(target=EvenFact, args=(iNo, ))
    thread2 = threading.Thread(target=OddFact, args=(iNo, ))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    print("Exit from main: ")
if __name__ == "__main__":
    main()