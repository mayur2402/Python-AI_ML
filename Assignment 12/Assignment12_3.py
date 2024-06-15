

import os
import sys

import psutil

def GetRunningProcess(FolderName):
    dictProcess = {}
    iCnt = 0
    for process in psutil.process_iter(["pid","name","username"]):
       dictProcess[iCnt] = process.info
       iCnt += 1

    if(os.path.isdir(FolderName) == False):
        FolderName = os.makedirs(FolderName)
    print(FolderName)
    if(os.path.isabs(FolderName) == False):
        FolderName = os.path.abspath(FolderName)

    fileName = "log.txt"

    FolderName = os.path.join(FolderName,fileName)

    f = open(FolderName,"w")
    f.write("PID\t\tNAME\t\tUSERNAME\n" )
    for data in dictProcess:
        f.write( str(dictProcess[data]["pid"]) +"\t")
        f.write("\t" +dictProcess[data]["name"] +"\t")
        f.write("\t" +str(dictProcess[data]["username"]) +"\n")

    f.close()

def main():

    if(len(sys.argv) != 2 ):
        print("Enter Valid Command Line Argument")

    GetRunningProcess(sys.argv[1])

if __name__ == "__main__":
    main()