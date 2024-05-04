import os
import multiprocessing

def task1(no):
    print("In Task1")
    print("Process id of task1 : ",os.getpid())
    print("parent Process id of task1 : ",os.getppid())

def task2(no):
    print("In Task2")
    print("Process id of task2 : ",os.getpid())
    print("parent Process id of task2 : ",os.getppid())

def main():
    print("Process id of main :",os.getpid())
    print("Parent Process id of main is ",os.getppid())

    Value = 11
    p1 = multiprocessing.Process(target = task1,args = (Value,))
    p2 = multiprocessing.Process(target = task2,args = (Value,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

if __name__ == "__main__":
    main()