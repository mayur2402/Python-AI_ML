

i = 1

def fun(no):
    global i
    if(no >= 1):
        print(no)
        no = no - 1
        fun(no)
        

def main():
    print("Enter number")
    no = int(input())
    fun(no)

if __name__ == "__main__":
    main()