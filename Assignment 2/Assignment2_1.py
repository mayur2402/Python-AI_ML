from Calculation import *

def main():
    print("Enter First Number")
    no1 = int(input())

    print("Enter Second Number")
    no2 = int(input())
    
    addition = Add(no1,no2)
    print("Addition is :",addition)

    substraction = Sub(no1,no2)
    print("Substraction is :",substraction)

    multiplication = Multi(no1,no2)
    print("Multiplication is :",multiplication)

    division = Div(no1,no2)
    print("Division is :",division)

if __name__ == "__main__":
    main()