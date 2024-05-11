class Circle:
    PI = 3.142
    def __init__(self):
        self.radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        print("Enter Radius of circle")
        self.radius = float(input())
        print(self.radius)

    def CalculateArea(self):
        global PI
        self.Area = Circle.PI * self.radius * self.radius

    def CalculateCircumference(self):
        global PI
        self.Area = 2 * Circle.PI * self.radius

    def Display(self):
        print("Radius of circle is ", self.radius)
        print("Area of circle is ", self.Area)
        print("Circumference of circle is ", self.Circumference)

def main():
    obj1 = Circle()
    obj1.Accept()
    obj1.CalculateArea()
    obj1.CalculateCircumference()
    obj1.Display()

    obj2 = Circle()
    obj2.Accept()
    obj2.CalculateArea()
    obj2.CalculateCircumference()
    obj2.Display()

if __name__ == "__main__":
    main()

