import os
import sys

def DirectoryWatcher(DirName):
    for foldername,subfldername,filename in os.walk(DirName):
        for name in filename:
            print(name)

def main():
    print("-----------------------------------------")
    
    print("Directory Watcher")
    
    print("-----------------------------------------")

    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This script is used to perform directory traversal")
            exit()
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Usage of script : ")
            print("Name_of_file Name of directory")
            exit()
        else:
            try:
                DirectoryWatcher(sys.argv[1])
            except Exception as ex:
                print("Exception occurs ", ex)

        
    else:
        print("Invalid Option")
        print("use --h option to get help or --u to get usages of script")
        exit()

    print("-----------------------------------------")
    
    print("Thanks for using MTD script")
    
    print("-----------------------------------------")
if __name__ == "__main__":
    main()