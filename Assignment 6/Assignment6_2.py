import threading


def evenfactor(no):
    if(no < 0):
        no = -no

    if(no == 1):
        return
    
    if(no == 2):
        print(2)

    half = int(no / 2)

    add = 0
    for i in range(2,half):
        if(no % i == 0):
            add = add + i
        
    if(no % 2 == 0):
        add = add + no

    print("Even factor addition ",add)

def oddfactor(no):
    if(no < 0):
        no = -no

    if(no == 2):
        return
    
    if(no == 1):
        print(1)

    half = int(no / 2)

    add = 0
    for i in range(1,half):
        if(no % i != 0):
            add = add + i
        
    if(no % 2 != 0):
        add = add + no

    print("Odd factor addition",add)

def main():
    print("Enter number")
    no = int(input())

    thread1 = threading.Thread(target=evenfactor,args=(no,))
    thread2 = threading.Thread(target=oddfactor,args=(no,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()