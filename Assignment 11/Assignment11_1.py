

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

def CheckSum(DirName):

    if os.path.isabs(DirName) == False:
        DirName = os.path.abspath(DirName)

    if os.path.exists(DirName) == False:
        print("Invalid Directory")

    for folderList,SubFolderList,FileList in os.walk(DirName):
        print("Current Directory is ")
        for filename in FileList:
            absPath = os.path.join(folderList,filename)
            fileHash = HashFile(absPath)
            print("%s is checksum of file %s" %(fileHash,absPath))

def main():

    if len(argv) != 2:
        print("InValid Directory Input")
        exit()

    CheckSum(argv[1])

if __name__ == "__main__":
    main()