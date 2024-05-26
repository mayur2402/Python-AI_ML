import filecmp
import os

def main():
    print("Enter first file name ")
    fname1 = input()

    print("Enter second file name ")
    fname2 = input()

    obj1 = open(fname1,"r")
    data1 = obj1.read()
    obj2 = open(fname2,"r")
    data2 = obj2.read()

    if filecmp.cmp(fname1,fname2,shallow=False):
        print("Success")
    else:
        print("Failure")
    
if __name__ == "__main__":
    main()