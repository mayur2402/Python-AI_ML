
def FactorSum(no):

    if no == 0:
        return 0
    
    if no < 0:
        no = -no

    sum = 0
    end = int(no/2)
    end = end + 1
    
    for num in range(1,end):
        if( no % num == 0):
            sum = sum + num
    
    return sum

def main():
    print("Enter number to find sum of its factors")
    no = int(input())

    sum = FactorSum(no)
    print(sum)

if __name__ == "__main__":
    main()