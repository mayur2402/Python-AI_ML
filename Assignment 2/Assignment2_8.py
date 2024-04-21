
def displayPattern(no):
    if no == 0:
        return
    
    if no < 0:
        no = -no

    for i in range(1,no+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()

def main():
    print("Enter number to display Pattern")
    no = int(input())

    displayPattern(no)


if __name__ == "__main__":
    main()