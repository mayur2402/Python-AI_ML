import os

def main():
    print("Enter file name ")
    name = input()

    if(os.path.exists(name) != True):
        demoobj = open("Demo.txt","r")
        data = demoobj.read()
        fobj = open(name,"w")
        fobj.write(data)
    else:
        print("File not present")

if __name__ == "__main__":
    main()