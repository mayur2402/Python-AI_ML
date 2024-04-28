

i = 1

def fun(no):
    global i
    if(i <= no):
        print(i)
        i = i + 1
        fun(no)
        

def main():
    print("Enter number")
    no = int(input())
    fun(no)

if __name__ == "__main__":
    main()