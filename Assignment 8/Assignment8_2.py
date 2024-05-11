class bankAccount:
    ROI = 10.5
    def __init__(self,Name,Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("Name of Customer is ",self.Name)
        print("Amount in bank is ",self.Amount)

    def Deposit(self):
        print("Enter amount to deposit")
        amount = float(input())
        self.Amount = self.Amount + amount

    def Withdraw(self):
        print("Enter amount to withdraw")
        amount = float(input())

        if(self.Amount < amount):
            print("Insufficient Balance")
            return
    
        self.Amount = self.Amount - amount

    def CaluculateInterest(self):
        interest = (self.Amount * bankAccount.ROI)/100
        print("Interest is ",interest)

def main():
    print("Enter name of customer")
    name = input()
    print("Enter amount ")
    amount = float(input())

    obj1 = bankAccount(name,amount)
    obj1.Deposit()
    obj1.Withdraw()
    obj1.CaluculateInterest()
    obj1.Display()

    print("Enter name of customer")
    name = input()
    print("Enter amount ")
    amount = float(input())

    obj2 = bankAccount(name,amount)
    obj2.Deposit()
    obj2.Withdraw()
    obj2.CaluculateInterest()
    obj2.Display()

if __name__ == "__main__":
    main()