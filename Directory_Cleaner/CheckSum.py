from sys import *
import os
import hashlib

def hashfile(path,blocksize = 1024):
    afile = open(path,'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)

    while(len(buf) > 0):
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()

def DisplayCheckSum(path):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    if exists:
        for dirname,subdirname,fileList in os.walk(path):
            print("Current folder is :" + dirname)

            for filen in fileList:
                path = os.path.join(dirname,filen)
                file_hash = hashfile(path)
                print(path)
                print(file_hash)
                print(' ')
    else:
        print("Invalid Path")

def main():

    print("---- Mayur Dimble ----")
    print("Application name : " + argv[0])

    if(len(argv) != 2):
        print("Error : Invalid Number of argument")
        exit()

    try:
        arr = DisplayCheckSum(argv[1])
    except Exception as E:
        print("Error Invalid Input ",E)


if __name__ == "__main__":
    main()
