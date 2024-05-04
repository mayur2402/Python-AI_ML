
def FindMinimum(list1):
    min = list1[0]
    for num in list1:
        if(min > num):
            min = num

    return min

def main():
    print("Enter number")
    no = int(input())
    list1 = []
    print("Enter numbers")
    for i in range(no):
        num = int(input())
        list1.append(num)

    min = FindMinimum(list1)

    print(min)

if __name__ == "__main__":
    main()