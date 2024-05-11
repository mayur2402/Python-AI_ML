class Demo:
    value = 0
    def __init__(self,no1,no2):
        self.no1 = no1
        self.no2 = no2

    def Fun(self):
        print(self.no1)
        print(self.no2)

    def Gun(self):
        print(self.no1)
        print(self.no2)


def main():
    ob1 = Demo(11,21)
    ob2 = Demo(51,101)

    ob1.Fun()
    ob1.Gun()
    ob2.Fun()
    ob2.Gun()

if __name__ == "__main__":
    main()