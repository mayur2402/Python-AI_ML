import os


def main():
    print("Enter name of file that you want to create : ")
    FName = input()
    if os.path.exists(FName):
        print("Unable to create file as file exists ")
    else:
        open(FName,"x")
        print("File Created Successfully ")
if __name__ == "__main__":
    main()