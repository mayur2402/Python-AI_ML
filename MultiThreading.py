import os

def main():
    print("PId of running process is : ",os.getpid())
    print("PId of parent Process i.e. command prompt is : ",os.getppid())

if __name__ == "__main__":
    main() 