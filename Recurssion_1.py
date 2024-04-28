
def fun(i):
    print ("in Fun" , i)
    i = i + 1
    fun(i)

j = 1
def funx():
    global j
    print ("in Fun" , j)
    j = j + 1
    funx()



def main():
    fun(1)
    
    funx()

if __name__ == "__main__":
    main()