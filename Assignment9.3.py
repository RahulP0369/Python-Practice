# Function Name :  CopyFileContents()  
#
# Description   :  program which accept file name from user and create new file named as Demo.txt and 
#                  copy all contents from existing file into new file. Accept file name through command line 
#                  arguments
#
# Input         :  string
#
# Output        : 
#
# Author        :  Rahul Patil

import sys
import os

def CopyFileContents(SourceFile, DestFile):
    if os.path.exists(SourceFile):
        print("File Exists")
    else:
        print("File does not exists")
    
    with open(SourceFile) as srcFile , open(DestFile,"w") as destFile:
        for line in srcFile:
            destFile.write(line)

    srcFile.close()
    destFile.close()

def main():
    print("---------Script----------")
    print("Script name: ",sys.argv[0])
    print("Number of an argument accepted: ",len(sys.argv)-1)

    if(len(sys.argv) > 3) or (len(sys.argv)<2):
        print("Invalid number of argument")
        print("Use -u flag for usage")
        print("Use -h flag for help")
        exit()

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "-u") or (sys.argv[1] == "-U"):
            print("Usage: Script is used to copy first contents to another")
            exit()

        elif(sys.argv[1] == "-h") or (sys.argv[1] == "-H"):
            print("Help: Name_of_Script First_Argument Second_Argument")
            print("First_Argument: Name of a source file")
            print("Second_Argument: Name of a destination file")
            exit()
        else:
            print("There is no such flag")
            exit()
    if(len(sys.argv) == 3):
        try:
            iRet = CopyFileContents(sys.argv[1], (sys.argv[2]))
        
        except Exception:
            print("Exception while executing the script")
            print("Please check input or contact the dev")

if __name__ == "__main__":
    main()