
sum = 1
def printStar(no):
    if(no < 0):
        no = -no
    global sum
    if(no != 0):
        sum = sum * no
        printStar(no-1)

    return sum

def main():
    print("Enter number ")
    no = int(input())

    sum = printStar(no)

    print(sum)

if __name__ == "__main__":
    main()