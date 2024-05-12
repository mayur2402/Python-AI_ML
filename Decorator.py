def sub(no1,no2):
    print(no1-no2)

def SmartSub(fptr):
    def Inner(a,b):
        if a < b:
            a,b = b,a
        return fptr(a,b)
    return Inner

sub = SmartSub(sub)

def main():
    no1 = int(input("Enter first number"))
    no2 = int(input("Enter second number"))

    sub(no1,no2)

if __name__ == "__main__":
    main()