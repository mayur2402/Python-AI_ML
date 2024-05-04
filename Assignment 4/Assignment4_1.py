power = lambda no : pow(no, 2) 

def main():
    print("Enter number whos power 2 you want")
    no = int(input())
    
    print(power(no))

if __name__ == "__main__":
    main()