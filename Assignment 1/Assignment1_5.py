def loop(no):
    if(no <= 0):
        print("Enter Valid number")
        return
    for i in range(no,0,-1):
        print(i ,end=" ")

def main():
    loop(10)

if __name__ == "__main__":
    main()