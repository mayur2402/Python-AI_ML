import multiprocessing.pool
import os
import time

def Cube(No):
    print("PID is ",os.getpid())
    return pow(No,3)

def main():
    starttime = time.time()
    Arr = [100000,200000,300000,400000,100000,200000,300000,400000,100000,200000,300000,400000,100000,200000,300000,400000]

    Result = []

    p = multiprocessing.Pool()
    Result = p.map(Cube,Arr)
    p.close()
    p.join()

    print(Result)
    endtime = time.time()

    print("Time Required is ",endtime-starttime)

if __name__ == "__main__":
    main()