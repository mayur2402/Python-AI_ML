import sys

def main():
    print("Name of application:",sys.argv[0])
    print("Data type of argv :", type(sys.argv))
    print("length of argv :", len(sys.argv))
    i = 0
    while(i < len(sys.argv)):
        print(sys.argv[i])
        i = i + 1
if(__name__ == "__main__"):
    main()

