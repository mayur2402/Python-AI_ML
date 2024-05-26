import os

def main():
    print("Enter file name ")
    name = input()

    print("Enter string you want to check")
    data = input()
    count = 0
    if(os.path.exists(name)):
        fobj = open(name,"r")
        lines = fobj.readlines()

        for line in lines:
            for word in line.split():
                if(word == data):
                    count = count + 1
    else:
        print("File not present")

    print("Count is " , count)
if __name__ == "__main__":
    main()