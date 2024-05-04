from FMRModule import filterV2
from FMRModule import mapV2
from FMRModule import reduceV2

ChechEvenlam = lambda no : no % 2 == 0
Increaselam = lambda no : no + 1
Addlam = lambda a,b: a+b

def main():
    print("Enter number of elements")
    no = int(input())
    data = []
    for i in range(no):
        print("Enter Number")
        num = int(input())
        data.append(num)

    FData = list(filterV2(ChechEvenlam,data))
    print("Data After filter activity",FData)

    Mdata = list(mapV2(Increaselam,FData))
    print("Data after map function",Mdata)
    
    RData = reduceV2(Addlam,Mdata)

    print("Data after reduce activity", RData)

if __name__ == "__main__":
    main()


