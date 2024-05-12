def main():
    ans = 0
    try:
        print("Enter First Number")
        no1 = int(input())

        print("Enter Second Number")
        no2 = int(input())

        ans = no1 / no2
    except ZeroDivisionError as zobj :
        print("Exception Occurs ",zobj)
    except ValueError as vobj:
        print("Exception occur ",vobj)
    except Exception as eobj:
        print("Exception Occur ",eobj)
    finally:
        print("Inside Finally block")

    print("Division is ", ans)

if __name__ == "__main__":
    main()