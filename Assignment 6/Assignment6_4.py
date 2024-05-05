import os
import threading


def DisplaySmallCount(string):
    count = 0
    for s in string:
        if(s >= 'a' and s <= 'z'):
            count = count + 1
    print("DisplaySmallCount pid ",os.getpid() , threading.current_thread().name)    
    print("Small characters count is ",count)


def DisplayCapitalCount(string):
    count = 0
    for s in string:
        if(s >= 'A' and s <= 'Z'):
            count = count + 1
    print("DisplayCapitalCount pid ",os.getpid() , threading.current_thread().name)    
    print("Capital characters count is ",count)

def DisplayNumberCount(string):
    count = 0
    for s in string:
        if(s.isnumeric()):
            count = count + 1
    print("DisplayNumberCount pid ",os.getpid() , threading.current_thread().name)    
    print("Number count is ",count)

def main():
    print("Enter string")
    string = input()

    thread1 = threading.Thread(target=DisplayCapitalCount,args=(string,))
    thread2 = threading.Thread(target=DisplaySmallCount,args=(string,))
    thread3 = threading.Thread(target=DisplayNumberCount,args=(string,))

    thread1.start()
    thread2.start()
    thread3.start()  
    
    thread1.join()
    thread2.join()
    thread3.join()

if __name__ == "__main__":
    main()