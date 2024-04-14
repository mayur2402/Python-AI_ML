def Addition(No1,No2):
    print("Inside Addition")
    Ans = 0
    Ans = No1 + No2
    return Ans

def main():
    print("Inside main")
    print("Enter First Number")
    A = int(input())

    print("Enter Second Number")
    B = int(input())

    Result = Addition(A,B)
    print("Addition is : ", Result)

main()
print("End of program")