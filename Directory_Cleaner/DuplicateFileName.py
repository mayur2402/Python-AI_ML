import hashlib
import os
from sys import argv

def hashFile(path,blockSize = 1024):

    binaryFile = open(path,'rb')
    hasher = hashlib.md5()

    buffer = binaryFile.read(blockSize)

    while(len(buffer) > 0):
        hasher.update(buffer)
        buffer = binaryFile.read(blockSize)
    
    binaryFile.close()
    return hasher.hexdigest()

def FindDuplicateFileName(dirName):

    if os.path.isabs(dirName) == False:
        dirName = os.path.abspath(dirName)

    if os.path.isdir(dirName) == False:
        print("Invalid Directory")
        exit()
    
    fileDict = {}
    for DNameList,SDNameList,FNameList in os.walk(dirName):
        print("Current Directory Name")

        for FileName in FNameList:
            path = os.path.join(dirName,FileName)
            fileHash = hashFile(path)
            if fileHash in fileDict:
                fileDict[fileHash].append(path)
            else:
                fileDict[fileHash] = [path]

    return fileDict

def printDuplicate(DictData):

    result = list(filter(lambda x : len(x) > 1,DictData.values()))

    if(len(result) > 1):
        print("Duplicate File Found")

        iCnt = 0

        for data in result:
            for sData in data:
                iCnt = iCnt + 1
                if iCnt >= 2:
                    print(sData)

            iCnt = 0

def main():

    print("-- Mayur Dimble --")
    print("Application name is ", argv[0])

    if len(argv) != 2:
        print("Invalid Input")
        exit()

    try:
        dictData = {}
        dictData = FindDuplicateFileName(argv[1])
        printDuplicate(dictData)
    except Exception as ex:
        print(ex)

if __name__ == "__main__":
    main()