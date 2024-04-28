def displayFor(no):
    if(no > 0):
        for i in range(1,no+1):
            print(i)


def displayWhile(no):
    if(no > 0):
        i = 1
        while(i <= no):
            print(i)
            i = i + 1


def main():
    displayFor(5)
    displayWhile(5)

if __name__ == "__main__":
    main()