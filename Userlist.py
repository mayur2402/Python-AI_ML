def main():
    print("Enter number of elements that you want to insert")
    size = int(input())

    arr = list()

    print("Enter element")

    for i in range(size):
        no = int(input())
        arr.append(no)
    print(arr)

    sum = addition(arr)
    print(sum)

def addition(arr):
    if(len(arr) > 1):
        sum = 0
        for num in range(len(arr)):
            sum = sum + arr[num]

        return sum
    return 0

if(__name__ == "__main__"):
    main()