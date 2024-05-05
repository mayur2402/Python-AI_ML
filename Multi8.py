import os


def Cube(No):
    print("PID is ",os.getpid())
    return pow(No,3)

def main():
    Arr = [10,20,30,40]

    Result = []

    for value in Arr:
        Result.append(Cube(value))

    print(Result)

if __name__ == "__main__":
    main()