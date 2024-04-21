def DivideByFive(no):
    if(no % 5 == 0):
        return True
    else:
        return False


def main():
    print("Enter Number")
    no = int(input())
    isdivide = DivideByFive(no)

    if(isdivide == True):
        print("Able to divide number by five")
    else:
        print("Not Able to divide number by five")
if __name__ == "__main__":
    main()