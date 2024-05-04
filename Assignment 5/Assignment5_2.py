
i = 1
def printStar(no):
    global i
    if(no > 0):
        print(i,end=" ")
        i = i + 1
        printStar(no-1)

def main():
    print("Enter number ")
    no = int(input())

    printStar(no)

if __name__ == "__main__":
    main()