print("Demo of Functional")

def Addition(no1,no2):
    Ans = no1 + no2
    return Ans

def Sub(no1,no2):
    Ans = no1 - no2
    return Ans

def main():
    print("Enter First number")
    no1 = int(input())

    print("Enter Second number")
    no2 = int(input())
    
    Ans = Addition(no1,no2)
    print("Addition is ",Ans)

    Ans = Sub(no1,no2)
    print("Sub is ",Ans)

if __name__ == "__main__":
    main()