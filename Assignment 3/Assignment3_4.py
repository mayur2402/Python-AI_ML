

def Compare(list1,num):
    count = 0

    for i in list1:
        if i == num:
            count = count + 1

    return count

def main():
    print("How many number")
    no = int(input())
    list1 = []
    print("Enter numbers")
    for i in range(no):
        num = int(input())
        list1.append(num)

    print("Enter number ")
    comp = int(input())

    freq = Compare(list1,comp)

    print(freq)


if __name__ == "__main__":
    main()