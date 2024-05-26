import os

def main():
    print("Enter file name ")
    name = input()

    if(os.path.exists(name)):
        fobj = open(name,"r")
        data = fobj.read()
        print(data)
    else:
        print("File not present")

if __name__ == "__main__":
    main()