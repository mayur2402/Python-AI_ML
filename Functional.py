print("Demo of functional")

Addition = lambda no1,no2: no1 + no2

Sub = lambda no1,no2 : no1 - no2

print("Enter First number")
no1 = int(input())

print("Enter Second number")
no2 = int(input())
    
Ans = Addition(no1,no2)
print("Addition is ",Ans)

Ans = Sub(no1,no2)
print("Sub is ",Ans)
