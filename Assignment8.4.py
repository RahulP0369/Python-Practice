from cgitb import small
import threading
from turtle import st
from unicodedata import digit

def Small(str):
    iCnt = 0

    for i in range (len(str)):
        if (str[i] >= 'a' and str[i] <= 'z'):
            iCnt = iCnt+1

    print("Count of Sapital characters are",iCnt)


def Capital(str):
    iCnt = 0

    for i in range(len(str)):
        if(str[i] >= 'A' and str[i] <= 'Z'):
            iCnt = iCnt+1
    print("Count of Capital Characters are: ",iCnt)

def Digit(str):
    iCnt = 0

    for i in range(len(str)):
        if(str[i] >= '0' and str[i] <= '9'):
            iCnt = iCnt+1
    print("Count of Digits in string are: ",iCnt)

def main():

    str = input("Enter String: \n")

    thread1 = threading.Thread(target=Small, args=(str, ))
    thread2 = threading.Thread(target=Capital, args=(str, ))
    thread3 = threading.Thread(target=Digit, args=(str, ))

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()

if __name__ == "__main__":
    main()