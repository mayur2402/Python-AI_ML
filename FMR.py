from functools import reduce

# Normal Function

def ChechEven(no):
    return (no % 2 == 0)

def Increase(no):
    return no + 1

def Add(a,b):
    return a+b

def main():
    print("Enter number of elements")
    no = int(input())
    data = []
    for i in range(no):
        print("Enter Number")
        num = int(input())
        data.append(num)
    
    print("Data From Input List",data)

    FData = list(filter(ChechEven,data))
    print("Data After filter activity",FData)

    Mdata = list(map(Increase,FData))
    print("Data after map function",Mdata)

    RData = reduce(Add,Mdata)

    print("Data after reduce activity", RData)

if __name__ == "__main__":
    main()