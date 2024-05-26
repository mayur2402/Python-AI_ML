import os


def main():
    print("Enter name of file that you want to create : ")
    FName = input()
    if os.path.exists(FName):
        fobj = open(FName,"r")
        print("File Open Successfully ")
    else:
        print("Unable to create file as file is not exists  ")

if __name__ == "__main__":
    main()