class Arithmetic:
    def __init__(self):
        self.value1 = 0
        self.value2 = 0

    def Accept(self):
        print("Enter Value 1")
        self.value1 = int(input())
        print("Enter Value 2")
        self.value2 = int(input())
        
    def Addition(self):
        return self.value1 + self.value2
    
    def Substraction(self):
        return self.value1 - self.value2

    def Multiplication(self):
        return self.value1 * self.value2
    
    def Division(self):
        if(self.value2 == 0):
            return 0
        return self.value1 / self.value2
    
def main():
    obj1 = Arithmetic()
    obj1.Accept()
    ans = obj1.Addition()
    print("Addition is ",ans)
    ans = obj1.Substraction()
    print("Substraction is ", ans)
    ans = obj1.Multiplication()
    print("Multiplication is ", ans)
    ans = obj1.Division()
    print("Division is ", ans)

    obj2 = Arithmetic()
    obj2.Accept()
    ans = obj2.Addition()
    print("Addition is ",ans)
    ans = obj2.Substraction()
    print("Substraction is ", ans)
    ans = obj2.Multiplication()
    print("Multiplication is ", ans)
    ans = obj2.Division()
    print("Division is ", ans)


if __name__ == "__main__":
    main()