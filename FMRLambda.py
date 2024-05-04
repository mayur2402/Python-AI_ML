from functools import reduce

def main():
    data = [11,14,20,23,18,16,15,20]
    print("Data From Input List",data)

    FData = list(filter(lambda no : no % 2 == 0,data))
    print("Data After filter activity",FData)

    Mdata = list(map(lambda no : no + 1,FData))
    print("Data after map function",Mdata)

    RData = reduce(lambda a,b: a+b,Mdata)

    print("Data after reduce activity", RData)

if __name__ == "__main__":
    main()