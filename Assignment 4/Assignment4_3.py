

from functools import reduce


def Filter7090(num):
    if(num >= 70 and num <= 90):
        return num

def Map10(num):
    return num + 10

def ReduceProduct(num1,num2):
    return num1 * num2


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

    list2 = list(filter(Filter7090,list1))

    print("List after filter : ",list2)

    list3 = list(map(Map10,list2))

    print("List after map : ",list3)

    ans = reduce(ReduceProduct,list3)

    print("Product is : ",ans)

if __name__ == "__main__":
    main()    
