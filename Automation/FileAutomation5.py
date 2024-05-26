import os
import sys
import time

def DirectoryWatcher(DirName):
    flag = os.path.isabs(DirName)
    print(os.path.abspath(DirName))
    if(flag == False):
        DirName = os.path.abspath(DirName)

    if(os.path.isdir(DirName)):
        for foldername,subfldername,filename in os.walk(DirName):
            
            print("Current Folder Name : " , foldername)

            for subname in subfldername:
                print("Sub Folder Name is " , subname)
            
            for name in filename:
                print(name)
    else:
        print("Invalid Directory name")

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
                starttime = time.time()
                DirectoryWatcher(sys.argv[1])
                endtime = time.time()
                totaltime = endtime - starttime
                print("Time require to execute script is ", totaltime)
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