def Addition(No1,No2,No3,No4):
    Ans = No1 + No2 + No3 + No4
    return Ans

Ans = Addition(10,20,30,50)
print(Ans)


def Additionvariable(*No):
    print(type(No))
    print(No)
    print(len(No))
    Ans = 0
    for i in No:
        Ans = Ans + i
    return Ans

Ans = Additionvariable(10,20,30)
print(Ans)

Ans = Additionvariable(10,20,30,40)
print(Ans)

Ans = Additionvariable(10,20,30,40,50)
print(Ans)
