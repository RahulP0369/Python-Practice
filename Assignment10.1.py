# Function Name :  FileExt()  
#
# Description   :  Automation script which accept directory name and file extension from user. Display all 
#                  files with that extension.
#
# Input         :  string
#
# Output        : 
#
# Author        :  Rahul Patil

from sys import *
import os

def FileExt(path,ext):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)
    
    if exists: 
    
        for DirectoryName, SubDirectory, Filename in os.walk(path):
            print("Current Directory is: "+DirectoryName)

            for SubD in SubDirectory:
                print("Sub folder of "+DirectoryName+"is: "+SubD)
            
            for file in Filename:
                if file.endswith(ext):
                    print(file)

            print(' ')
    else:
        print("Invalid Path")

def main():

    print("----------The Automation Script To accept name and file from user and  Display all files with that extension---------")

    print("Application name: "+argv[0])

    if(len(argv) != 3):
        print("Error: Invalid number of an arguments")
        exit()

    if(argv[1] == "-h") or (argv[1] == "-H"):
        print("This script is used to traverse  specific directory")
        exit()

    if(argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage: ApplicationName AbsolutePath_of_Directory  Extension_Name")
        exit()
    
    try:
        FileExt(argv[1],argv[2])

    except ValueError:
        print("Error: Invalid datatype of an input")

    except Exception:
        print("Error: Invalid input")

if __name__ == "__main__":
    main()
