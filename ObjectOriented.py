print("Demo of object oriented")

class Arithmetic:
    def __init__(self,value1,value2):
       self.no1 = value1
       self.no2 = value2

    def Addition(self):
        ans = self.no1 + self.no2
        return ans

    def Substraction(self):
        ans = self.no1 - self.no2
        return ans

def main():
    print("Enter First number")
    no1 = int(input())

    print("Enter Second number")
    no2 = int(input())
    
    obj = Arithmetic(no1,no2)

    Ans = obj.Addition()
    print("Addition is ",Ans)

    Ans = obj.Substraction()
    print("Sub is ",Ans)

if __name__ == "__main__":
    main()