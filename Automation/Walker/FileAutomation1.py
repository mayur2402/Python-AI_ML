import sys

def Addition(A,B):
    return A+B

def main():
    print("-----------------------------------------")
    
    print("Automation for addition")
    
    print("-----------------------------------------")

    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This script is used to perform addition of two integral number")
            exit()
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Usage of script : ")
            print("Name_of_file First_Argument Second_Argument")
            print("Note : Both the arguments should be in the integral format")
            exit()
        else:
            print("Invalid Option")
            print("use --h option to get help or --u to get usages of script")
            exit()

    if(len(sys.argv) == 3):
        try:
            ret = Addition(int(sys.argv[1]),int(sys.argv[2]))
            print(ret)
        except ValueError as ex:
            print("Exception occurs invalid input please enter valid integer")
        except Exception as ex:
            print("Unable to perform the task due to ",ex)
    
    else:
        print("Invalid Option")
        print("use --h option to get help or --u to get usages of script")
        exit()

    print("-----------------------------------------")
    
    print("Thanks for using MTD script")
    
    print("-----------------------------------------")
if __name__ == "__main__":
    main()