

import hashlib
import os
from sys import argv
import time

def HashFile(path,blocksize = 1024):
    hasher = hashlib.md5()
    try:
        binaryFile = open(path,'rb')
        buffer = binaryFile.read(blocksize)
        while(len(buffer) > 0):
            hasher.update(buffer)
            buffer = binaryFile.read(blocksize)

        binaryFile.close()
    except Exception as ex:
        print(ex)
    return hasher.hexdigest()

def CheckSum(DirName):

    if os.path.isabs(DirName) == False:
        DirName = os.path.abspath(DirName)

    if os.path.exists(DirName) == False:
        print("Invalid Directory")

    dirCheckSum = {}
    for folderList,SubFolderList,FileList in os.walk(DirName):
        print("Current Directory is ",folderList)
        for filename in FileList:
            absPath = os.path.join(folderList,filename)
            fileHash = HashFile(absPath)
            if fileHash in dirCheckSum:
                dirCheckSum[fileHash].append(absPath)
            else:
                dirCheckSum[fileHash] = [absPath]

    return dirCheckSum

def RemoveDuplicateFile(DirCheckSum,fileName):
    starttime = time.time()
    if os.path.isabs(fileName) == False:
        logfile = os.path.abspath(fileName)
    
    log = open(fileName,'w')

    result = list(filter(lambda x : len(x) > 1,DirCheckSum.values()))


    if(len(result) > 1):
        log.write("Duplicate Files present" + "\n")
        icnt = 0
        for filedata in result:
            for filepath in filedata:
                icnt = icnt + 1
                if icnt >= 2:
                    log.write("File deleted " + filepath + "\n")
                    try:
                        os.remove(filepath)
                    except Exception as ex:
                        log.write("Exception occurs ", ex)

    Endtime = time.time()
    log.write(str(Endtime - starttime))
    log.close()
def main():

    if len(argv) != 3:
        print("InValid Directory Input and log file")
        exit()

    CheckSumData = {}
    CheckSumData = CheckSum(argv[1])
    RemoveDuplicateFile(CheckSumData,argv[2])

if __name__ == "__main__":
    main()