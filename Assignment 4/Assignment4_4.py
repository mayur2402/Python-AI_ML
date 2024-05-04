
from functools import reduce


filtereven = lambda num : num % 2 == 0 

mapSquare = lambda num : pow(num,2)

reduceaddition = lambda num1,num2 : num1 + num2


def main():
    print("How many numbers you want to filter")
    no = int(input())

    if(no <= 0):
        print("Enter valid numbers")
        return
    
    list1 = []
    print("Enter numbers")
    for i in range(no):
        num = int(input())
        list1.append(num)

    print("List is : ",list1)

    list2 = list(filter(filtereven,list1))

    print(list2)

    list3 = list(map(mapSquare,list2))

    print(list3)

    ans = reduce(reduceaddition,list3)

    print(ans)

if __name__ == "__main__":
    main()
