
def DisplayStar(no):
    if(no <= 0):
        print("Please enter valid number")
    for i in range(no):
        print("*",end=" ")


def main():
    print("Enter Number")
    no = int(input())
    DisplayStar(no)

if __name__ == "__main__":
    main()