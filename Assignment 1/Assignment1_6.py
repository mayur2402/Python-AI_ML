def CheckNum(no):
    if(no == 0):
        print("Number is Zero")
    elif(no < 0):
        print("Number is Negative")
    else:
        print("Number is positive")


def main():
    print("Enter Number")
    no = int(input())
    CheckNum(no)

if __name__ == "__main__":
    main()