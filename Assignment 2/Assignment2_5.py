
def checkPrime(no):
    if no == 0:
        return 0
    
    if no < 0:
        no = -no

    prime = False
    end = int(no/2)
    end = end + 1
    
    for num in range(2,end):
        if( no % num == 0):
            prime = True
        if prime == True:
            break

    if prime == False:
        print("Number is Prime Number")
    else:
        print("Number is not prime number")

def main():
    print("Enter number to check prime or not")
    no = int(input())

    checkPrime(no)

if __name__ == "__main__":
    main()