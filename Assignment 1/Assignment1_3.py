def Add(no1,no2):
    ans = no1 + no2
    return ans

def main():
    print("Enter first number")
    no1 = int(input())
    print("Enter Second number")
    no2 = int(input())

    ans = Add(no1,no2)
    print("Addition is :",ans)

if __name__ == "__main__":
    main()