# Function Name :  ChkFileExists()  
#
# Description   :  program which accepts file name from user and check whether that file exists in 
#                  current directory or not.
#
# Input         :  string
#
# Output        : 
#
# Author        :  Rahul Patil

import os
import sys

def ChkFileExists(name):

    if os.path.exists(name):
        print("File exists")

    else:   
        fd = open(name,"x")

        print("File opened sucessfully: ",fd)

def main():

    Ret = ChkFileExists(sys.argv[1])

if __name__ == "__main__":
    main()