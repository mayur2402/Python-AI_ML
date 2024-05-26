import os

def main():
    print("Enter name of file that you want to open for reading purpose : ")
    FName = input()
    if os.path.exists(FName):
        fobj = open(FName,"r")
        print("File Open Successfully in read mode ")
        str1 = fobj.readline()
        print(str1)
        str2 = fobj.readline()
        print(str2)
        str3 = fobj.readline()
        print(str3)
        str4 = fobj.readline()
        print(str4)
        # str5 = fobj.readline()
        # print(str5)
        fobj.close()
    else:
        print("Unable to create file as file is not exists  ")
if __name__ == "__main__":
    main()