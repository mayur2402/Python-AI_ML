import os

def main():
    print("Enter name of file that you want to open for writing purpose : ")
    FName = input()
    if os.path.exists(FName):
        fobj = open(FName,"w")
        print("File Open Successfully in write mode ")
        print("Enter data you want to write in file")
        data = input()
        fobj.write(data)

    else:
        print("Unable to create file as file is not exists  ")
if __name__ == "__main__":
    main()