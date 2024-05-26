import os

def main():
    print("Enter name of file that you want to open for reading purpose : ")
    FName = input()
    if os.path.exists(FName):
        os.remove(FName)
    else:
        print("Unable to create file as file is not exists  ")
if __name__ == "__main__":
    main()