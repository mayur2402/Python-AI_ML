import threading
import os

def printEven(arr):
    i = 2
    print("PID of print even",os.getpid())
    print("Even Numbers are :")
    for j in range(arr):
        print("Even Number ",i)
        i = i +2

def printOdd(arr):
    i = 1
    print("PID of print odd",os.getpid())
    print("Odd Numbers are :")
    for j in range(arr):
        print("Odd Number",i)
        i = i +2

def main():
    print("How many Number")
    print("PID of main",os.getpid())

    no = int(input())

    procss1 = threading.Thread(target=printEven,args=(no,))
    procss2 = threading.Thread(target=printOdd,args=(no,))
    
    # wrong way of programming not usefull for parallel program

    procss1.start()
    procss2.start()
    procss1.join()
    procss2.join()

    print("End of main")

if __name__ == "__main__":
    main()