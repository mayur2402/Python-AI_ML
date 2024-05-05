import multiprocessing

def printEven(arr):
    i = 2
    print("Even Numbers are :")
    for j in range(arr):
        print(i)
        i = i +2

def printOdd(arr):
    i = 1
    print("Odd Numbers are :")
    for j in range(arr):
        print(i)
        i = i +2

def main():
    print("How many Number")
    no = int(input())

    procss1 = multiprocessing.Process(target=printEven,args=(no,))
    procss2 = multiprocessing.Process(target=printOdd,args=(no,))
    
    # wrong way of programming not usefull for parallel program

    procss1.start()
    procss1.join()

    procss2.start()
    procss2.join()

    print("End of main")

if __name__ == "__main__":
    main()