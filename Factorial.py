
ans = 1

def fun(no):
    global ans
    if(no >= 1):
        ans = ans * no
        no = no - 1
        fun(no)
        

def main():
    print("Enter number")
    no = int(input())
    fun(no)
    print(ans)

if __name__ == "__main__":
    main()