

def Addition(No):
    add = 0
    for i in No:
        add = add + i

    return add

def main():
    print("How many numbers you want to add")
    no = int(input())

    numList = []

    print("Enter Numbers ")
    for i in range(no):
        num = int(input())
        numList.append(num)

    ans = Addition(numList)
    print("Addition is ",ans)