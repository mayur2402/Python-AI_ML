
def FindMaximum(list1):
    max = list1[0]
    for num in list1:
        if(max < num):
            max = num
    
    return max

def main():
    print("Enter Number")
    no = int(input())

    list1 = []
    print("Enter numbers ")
    for i in range(no):
        num = int(input())
        list1.append(num)

    max = FindMaximum(list1)

    print(max)

if __name__ == "__main__":
    main()