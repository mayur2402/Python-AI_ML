
def displayPattern(no):
    if no == 0:
        return
    
    if no < 0:
        no = -no

    for i in range(no,0,-1):
        for j in range(i,0,-1):
            print("*",end=" ")
        print()

def main():
    print("Enter number to display pattern")
    no = int(input())

    displayPattern(no)

if __name__ == "__main__":
    main()