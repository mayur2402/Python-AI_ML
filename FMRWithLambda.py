from functools import reduce

ChechEvenlam = lambda no : no % 2 == 0

Increaselam = lambda no : no + 1

Addlam = lambda a,b: a+b

def main():
    data = [11,14,20,23,18,16,15,20]
    print("Data From Input List",data)

    FData = list(filter(ChechEvenlam,data))
    print("Data After filter activity",FData)

    Mdata = list(map(Increaselam,FData))
    print("Data after map function",Mdata)

    # 15,21,19,17,21
    #0 + 15 = 15
    #15 + 21 = 36
    #36 + 19 = 55
    #55 + 17 = 72
    #72 + 21 = 93
    RData = reduce(Addlam,Mdata)

    print("Data after reduce activity", RData)

if __name__ == "__main__":
    main()