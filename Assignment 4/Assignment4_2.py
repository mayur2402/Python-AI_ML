
multiplication = lambda no1, no2 : no1 * no2

def main():
    print("Enter First Number")
    no1 = int(input())

    print("Enter Second Number")
    no2 = int(input())
    
    ans = multiplication(no1,no2)

    print(ans)

if __name__ == "__main__":
    main()