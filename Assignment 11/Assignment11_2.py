

import hashlib
import os
from sys import argv

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

def CheckSum(DirName,logfile):

    if os.path.isabs(DirName) == False:
        DirName = os.path.abspath(DirName)

    if os.path.exists(DirName) == False:
        print("Invalid Directory")

    if os.path.isabs(logfile) == False:
        logfile = os.path.abspath(logfile)

    log = open(logfile,'a')

    for folderList,SubFolderList,FileList in os.walk(DirName):
        print("Current Directory is ",folderList)
        for filename in FileList:
            absPath = os.path.join(folderList,filename)
            fileHash = HashFile(absPath)
            log.write("%s is checksum of file %s" %(fileHash,absPath) + "\n")

def main():

    if len(argv) != 3:
        print("InValid Directory Input and log file")
        exit()

    CheckSum(argv[1],argv[2])

if __name__ == "__main__":
    main()