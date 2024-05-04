
sum = 0
def printStar(no):
    global sum
    if(no != 0):
        rem = int(no%10)
        sum = sum + rem
        printStar(int(no/10))
    return sum

def main():
    print("Enter number ")
    no = int(input())

    sum = printStar(no)

    print(sum)

if __name__ == "__main__":
    main()