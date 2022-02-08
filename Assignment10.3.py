# Function Name :  RenameFileExt()  
#
# Description   :  Automation script which accept two directory names. Copy all files from first directory 
#                  into second directory. Second directory should be created at run time
#
# Input         :  string
#
# Output        : 
#
# Author        :  Rahul Patil

from sys import *
import os
import shutil

def CopyFiles(path, NewDir):

    flag = os.path.isabs(path)

    if flag == False:
        path = os.path.abspath(path) 

    exists = os.path.isdir(path)
    
    if exists:
        
        os.mkdir(NewDir)

        for DirectoryName, SubDirectory, Filename in os.walk(path):
            print("Current Directory is: "+DirectoryName)

            for SubD in SubDirectory:
                print("Sub folder of "+DirectoryName+"is: "+SubD)
            
            for file in Filename:

                srcFile = os.path.join(path, file)
                dstFile = os.path.join(NewDir,file)
                shutil.copy(srcFile, dstFile)

            print("File Copied sucessfully in: "+dstFile)
            print(' ')
    else:
        print("Invalid Path")

def main():

    print("----------Automation Script to copy all files to another directory---------")

    print("Application name: "+argv[0])

    if(len(argv) != 3):
        print("Error: Invalid number of an arguments")
        exit()

    if(argv[1] == "-h") or (argv[1] == "-H"): 
        print("This script is used to copy files from one directory another directory")
        exit()

    if(argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage: ApplicationName AbsolutePath_of_Directory New_File_Name")
        exit()
    
    try:
        CopyFiles(argv[1],argv[2])

    except ValueError:
        print("Error: Invalid datatype of an input")

    except Exception:
        print("Error: Invalid input")

if __name__ == "__main__":
    main()
