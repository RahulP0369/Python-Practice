# Function Name :  DisplayFileContents()  
#
# Description   :  program which accept file name from user and open that file and display the contents 
#                  of that file on screen
#
# Input         :  string
#
# Output        : 
#
# Author        :  Rahul Patil

import os
import sys

def DisplayFileContents(name):

    if os.path.exists(name):
        fd = open(name,"r")

        data = fd.read()
        print("Data from file is: ",data)

        fd.close()
    else:

        print("There is no such file or directory")

def main():

    ret  = DisplayFileContents(sys.argv[1]) 

if __name__ == "__main__":
    main()