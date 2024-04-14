import Marvellous as M
def main():
    
    print("Enter First Number")
    A = int(input())

    print("Enter Second Number")
    B = int(input())

    Ans = M.Addition(A,B)
    print("Addition is : ",Ans)

    Ans = M.Multiplication(A,B)
    print("Multiplication is : ",Ans)

main()