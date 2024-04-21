
def factorial(no):
    if(no == 0):
        return
    
    ans = 1
    if no < 0:
        no = -no
    for i in range(no,1,-1):
        ans = ans * i

    return ans

def main():
    print("Enter number to factorial")
    no = int(input())

    ans = factorial(no)
    print("Factoral is :", ans)

if __name__ == "__main__":
    main()