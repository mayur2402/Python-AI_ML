def Calculation(No1,No2):
    def Addition(X,Y):
        Add = X + Y
        return Add
    
    def Substraction(X,Y):
        Sub = X - Y
        return Sub
    
    Ans1 = Addition(No1,No2)
    Ans2 = Substraction(No1,No2)
    return Ans1,Ans2

print("Enter First Number")
A = int(input())

print("Enter Second Number")
B = int(input())

Result1,Result2 = Calculation(A,B)

print("Addition is : ", Result1)
print("Subtraction is : ", Result2)