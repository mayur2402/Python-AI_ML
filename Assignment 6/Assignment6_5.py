import threading


def OneToFifty():
    print("One To Fifty")
    for i in range(1,51):
        print(i,end=" ")
    print()

def FiftyToOne():
    print("Fifty To One")
    for i in range(50,0,-1):
        print(i,end=" ")
    print()

def main():
    thread1 = threading.Thread(target=OneToFifty)
    thread2 = threading.Thread(target=FiftyToOne)

    thread1.start()
    thread1.join()

    thread2.start()
    thread2.join()
    
if __name__ == "__main__":
    main()