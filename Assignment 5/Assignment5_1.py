

def printStar(no):
    if(no > 0):
        print("*",end=" ")
        printStar(no-1)

def main():
    print("Enter number ")
    no = int(input())

    printStar(no)

if __name__ == "__main__":
    main()