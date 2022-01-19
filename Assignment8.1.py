# Function Name :  FactR()  
#
# Description   :  recursive program which accept number from user and return its 
#                  factorial.
#
# Input         :  Integer
#
# Output        :  Integer
#
# Author        :  Rahul Patil

import threading

def Even():
   
    for i in range(1, 10):
        if ((i % 2) == 0):
            print("even number is: ",i)

def Odd():

    for j in range(1,10):
        if((j % 2) != 0):
            print("odd number is: ",j)

def main():

    thread1 = threading.Thread(target=Even, args=())
    thread2 = threading.Thread(target=Odd, args=())

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

if __name__ == "__main__":
    main()
