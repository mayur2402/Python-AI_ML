
def DisplayStar(no):
    i = 0 
    j = 1
    while i != no:
        if(j % 2 == 0):
            print(j , end=" ")
            i = i + 1
        j = j + 1


def main():
    DisplayStar(10)

if __name__ == "__main__":
    main()