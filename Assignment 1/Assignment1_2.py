def CheckNum(no):
    if(no % 2 == 0):
        print("Even Number")
    else:
        print("Odd Number")

def main():
    print("Enter Number")
    no = int(input())
    CheckNum(no)

if __name__ == "__main__":
    main()