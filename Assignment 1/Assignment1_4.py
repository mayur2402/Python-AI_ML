def loop(no,text):
    if(no <= 0):
        print("Enter Valid number")
        return
    for i in range(no):
        print(text)

def main():
    loop(5,"Marvellous")

if __name__ == "__main__":
    main()