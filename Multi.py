import threading

def printEven(arr):
    for i in arr:
        if(i % 2 == 0):
            print("Number "+ str(i) + " is even")

def printOdd(arr):
    for i in arr:
        if(i % 2 != 0):
            print("Number "+ str(i) + " is Odd")

def main():
    print("How many Number")
    no = int(input())

    arr = []
    print("Enter number")
    for i in range(no):
        num = int(input())
        arr.append(num)

    # printEven(arr)
    # printOdd(arr)

    thread1 = threading.Thread(target=printEven,args=(arr,))
    thread2 = threading.Thread(target=printOdd,args=(arr,))
    
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

if __name__ == "__main__":
    main()