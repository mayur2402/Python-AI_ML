
def  addDigits(no):
    if no == 0:
        return
    
    if no < 0:
        no = -no
    sum = 0
    while no != 0:
        digit = int(no %10)
        no = int(no / 10)

        sum = sum + digit
    return sum

def main():
    print("Enter number to add digits")
    no = int(input())

    sum = addDigits(no)
    print(sum)

if __name__ == "__main__":
    main()