import os

def main():
    print("Enter the name of directory that you want to scan :")
    Dname = input()

    print("List of files in folder are :")
    for folder ,subfolder,filname in os.walk(Dname):
        for fname in filname:
            print(fname)
        print(folder)
        print(subfolder)
if __name__ == "__main__":
    main()