import sys

def addition(no1,no2):
    ans = no1 + no2
    return ans

def main():
    if(len(sys.argv) == 3):
        no1 = int(sys.argv[1])
        no2 = int(sys.argv[2])
        
        ans = addition(no1,no2)
        print("addition is :", ans)
    else:
        print("Enter two number in command line")

if(__name__ == "__main__"):
    main()
