import os

def main():
    print("Enter file name ")
    name = input()

    if(os.path.exists(name)):
        print("File Present ")
    else:
        print("File not present")

if __name__ == "__main__":
    main()