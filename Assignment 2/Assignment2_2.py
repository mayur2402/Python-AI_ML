
def displayPattern(no):
    if(no == 0):
        return
    if(no < 0):
        no = -(no)

    for i in range(no):
        for j in range(no):
            print("*",end=" ")
        print()

def main():
    print("Enter number to display pattern")
    no = int(input())

    displayPattern(no)


if __name__ == "__main__":
    main()