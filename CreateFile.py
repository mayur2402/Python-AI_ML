import os


def main():
    print("Enter name of file that you want to create : ")
    FName = input()
    try:
        open(FName,"x")
    except FileExistsError as fobj:
        print("Exception Occurs :",fobj)
if __name__ == "__main__":
    main()