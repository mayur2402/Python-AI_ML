class Number:
    def __init__(self,value):
        self.value = value

    def factor(self):
        if(self.value < 0):
            self.value = -self.value

        if(self.value == 1):
            return
        
        if(self.value == 2):
            print(2)

        half = int(self.value / 2)
        print("Factors are")
        for i in range(1,half+1):
            if(self.value % i == 0):
                print(i  ,end=",")

        print()
        
    def Sumfactor(self):
        if(self.value < 0):
            self.value = -self.value

        if(self.value == 1):
            return
        
        if(self.value == 2):
            print(2)
            return

        half = int(self.value / 2)

        add = 0
        for i in range(1,half+1):
            if(self.value % i == 0):
                add = add + i

        print("Addition of factors ",add)

    def checkPrime(self):
        isprime = True
        for j in range(2,self.value-1):
            if self.value % j == 0:
                    isprime = False

        if(isprime):
            print("Number is prime")
        else:
            print("Number is not prime")

    def PerfectNumber(self):
        if(self.value < 0):
            self.value = -self.value

        if(self.value == 1):
            return
        
        if(self.value == 2):
            print(2)
            return

        half = int(self.value / 2)

        add = 0
        for i in range(1,half+1):
            if(self.value % i == 0):
                add = add + i

        if(add == self.value):
            print("Number is perfect number")
        else:
            print("Number is not perfect number")


def main():
    print("Enter number")
    value = int(input())

    obj1 = Number(value)
    obj1.checkPrime()
    obj1.Sumfactor()
    obj1.PerfectNumber()
    obj1.factor()


    print("Enter number")
    value = int(input())

    obj1 = Number(value)
    obj1.checkPrime()
    obj1.Sumfactor()
    obj1.PerfectNumber()
    obj1.factor()


if __name__ == "__main__":
    main()