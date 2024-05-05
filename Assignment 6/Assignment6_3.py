
import threading


def evenAddition(list1):
    add = 0
    for i in list1:
        if(i % 2 == 0):
           add = add + i

    print("Even number addition is ",add)


def oddAddition(list1):
    add = 0
    for i in list1:
        if(i % 2 != 0):
           add = add + i

    print("Odd number addition is ",add)

def main():
    print("How many numbers")
    no = int(input())

    if(no <= 0):
        return
    
    list1 = []
    print("Enter numbers")
    for i in range(no):
        num = int(input())
        list1.append(num)

    thread1 = threading.Thread(target=evenAddition,args=(list1,))
    thread2 = threading.Thread(target=oddAddition,args=(list1,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

if __name__ == "__main__":
    main()