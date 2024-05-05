

import threading


def even(no):
    if no <= 0:
        return
    i = 2
    j = 1
    while(j <= no) :
        if(i % 2 == 0):
            print(i)
            j = j + 1
        i = i + 1


def odd(no):
    if no <= 0:
        return
    i = 1
    j = 1
    while(j <= no) :
        if(i % 2 != 0):
            print(i)
            j = j + 1
        i = i + 1


def main():

    print("How many even and odd numbers")
    no = int(input())

    thread1 = threading.Thread(target=even,args=(no,))
    thread2 = threading.Thread(target=odd,args=(no,))
    
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

if __name__ == "__main__":
    main()