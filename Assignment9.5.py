# Function Name :  CmpFileContents()  
#
# Description   :  Accept file name and one string from user 
#                  and return the frequency of that string from file.
#
# Input         :  string
#
# Output        : 
#
# Author        :  Rahul Patil

import sys
import os

def FileContentsCounter(SourceFile,str1):
    iCnt = 0

    if os.path.exists(SourceFile):
        print("File Exists")
    else:
        print("File Does not exists")
    
    with open(SourceFile, "r") as fd:
        for FileLine in fd:
            str2 = FileLine.split()
            for i in str2:
                if(i == str1):
                    iCnt = iCnt+1
    print("Number of occurence of given string is")
    print(iCnt)

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
            print("Usage: Script is used to compare contents of files")
            exit()

        elif(sys.argv[1] == "-h") or (sys.argv[1] == "-H"):
            print("Help: Name_of_Script First_Argument Second_Argument")
            print("First_Argument: Name of a source file")
            print("Second_Argument: Name of a string to count it's frequency")
            exit()
        else:
            print("There is no such flag")
            exit()
    if(len(sys.argv) == 3):
        #try:
            iRet = FileContentsCounter(sys.argv[1],sys.argv[2])
        
        #except Exception:
            #print("Exception while executing the script")
            #print("Please check input or contact the dev")

if __name__ == "__main__":
    main()