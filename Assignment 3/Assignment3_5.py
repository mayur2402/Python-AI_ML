
def checkPrime(num):
    sum = 0
    for i in num:
        isprime = True
        for j in range(2,i-1):
            if i % j == 0:
                isprime = False

        if(isprime):
            sum = sum + i
    return sum

def main():
    print("How many numbers you want to enter")
    no = int(input())
    list1 = []

    print("Enter Numbers")
    for i in range(no):
        num = int(input())
        list1.append(num)
    
    num = checkPrime(list1)

    print(num)
    
if __name__ == "__main__":
    main()