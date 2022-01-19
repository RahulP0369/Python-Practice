from itertools import count
import threading

def Display():
    for i in range(0,50):
        print(i+1)
def DisplayRev():
    
    print("In reverse Order: \n")
    for i in range(50,0,-1):
        print(i)
def main():

    thread1 = threading.Thread(target=Display, args=())
    thread2 = threading.Thread(target=DisplayRev, args=())

    thread1.start()

    thread1.join()

    thread2.start()
if __name__ == "__main__":
    main()