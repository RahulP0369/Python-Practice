# Function Name :  CmpFileContents()  
#
# Description   :  program which accept two file names from user and compare contents of both the 
#                  files. If both the files contains same contents then display success otherwise display failure. 
#                  Accept names of both the files from command line
#
# Input         :  string
#
# Output        : 
#
# Author        :  Rahul Patil

import sys
import os

def CmpFileContents(SourceFile, DestFile):
    
    if os.path.exists(SourceFile):
        print("File Exists")

    else:
        print("File does not exists")
    
    with open(SourceFile, "r") as srcFile , open(DestFile,"r") as destFile:
        for FirstFileline in srcFile:
            for SecondFileLine in destFile:
                if FirstFileline == SecondFileLine:
                    print("Content in the both files are same")

                else:
                    print("Content in the both files are not equal")
    
def main():
    print("---------Automation Script----------")
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
            iRet = CmpFileContents(sys.argv[1], (sys.argv[2]))
        
        except Exception:
            print("Exception while executing the script")
            print("Please check input or contact the dev")

if __name__ == "__main__":
    main()