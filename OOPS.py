class  Demo:

    Data1 = 11
    Data2 = 21

    def __init__(self,A,B):
        print("Inside Constructor __init__")
        self.no1 = A
        self.no2 = B

    def Display(self):
        print("Value of no1 from display ",self.no1)
        print("Value of no2 from display ",self.no2)
        print("Value of Data1 from display ",Demo.Data1)
        print("Value of Data2 from display ",Demo.Data2)    
obj1 = Demo(10,20)
obj2 = Demo(30,40)

print("Value of no1 from obj1 : ",obj1.no1)
print("Value of no2 from obj1 : ",obj1.no2)

print("Value of no1 from obj2 : ",obj2.no1)
print("Value of no2 from obj2 : ",obj2.no2)

print("Value of Data1 : ",Demo.Data1)
print("Value of Data1 : ",Demo.Data2)

obj1.Display()
obj2.Display()