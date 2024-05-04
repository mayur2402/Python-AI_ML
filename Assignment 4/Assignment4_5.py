
from functools import reduce

def filterprime(list1):
    primelist = []
    isprime = True
    for num in list1:
        for i in range(2,num-1):
            if(num % i == 0):
                isprime = False
        if(isprime):
            primelist.append(num)
    return primelist

mapmultiple2 = lambda num : pow(num,2)

def maximum(list1):
    max = list1[0]

    for i in list1:
        if(max < i):
            max = i
    return max

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

    list2 = list(filterprime(list1))

    print(list2)

    list3 = list(map(mapmultiple2,list2))

    print(list3)

    ans = maximum(list3)

    print(ans)

if __name__ == "__main__":
    main()