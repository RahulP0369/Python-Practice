# Function Name :  RenameFileExt()  
#
# Description   :  Automation script which accept directory name and two file extensions from user. 
#                  Rename all files with first file extension with the second file extenntion
#
# Input         :  string
#
# Output        : 
#
# Author        :  Rahul Patil

from sys import *
import os

def RenameFileExt(path,ext1,ext2):

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

                NewPathX = os.path.join(path,file)
                
                newext = NewPathX.replace(ext1, ext2)
                os.rename(NewPathX, newext)

            print("Extension changed sucessfully")
            print(' ')
    else:
        print("Invalid Path")

def main():

    print("----------Automation script to rename all files with first file extension with the second file extensions---------")

    print("Application name: "+argv[0])

    if(len(argv) != 4):
        print("Error: Invalid number of an arguments")
        exit()

    if(argv[1] == "-h") or (argv[1] == "-H"): 
        print("This script is used to  to rename all files with first file extension with the second file extensions")
        exit()

    if(argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage: ApplicationName AbsolutePath_of_Directory First_Extenstion_Name Second_Extension_Name")
        exit()
    
    try:
        RenameFileExt(argv[1],argv[2],argv[3])

    except ValueError:
        print("Error: Invalid datatype of an input")

    except Exception:
        print("Error: Invalid input")

if __name__ == "__main__":
    main()
