import os
import sys

def DirectoryWatcher(dirname,fname):

    if(os.path.isabs(dirname) == False):
        dirname = os.path.abspath(dirname)

    for foldername,_,filename in os.walk(dirname):

        for name in filename:
            _,extension = os.path.splitext(os.path.join(foldername,name))
            if(extension.lower() == fname.lower()):
                print(os.path.join(foldername,name))

def main():
    
    if(len(sys.argv) == 3):
        DirectoryWatcher(sys.argv[1],sys.argv[2])

if __name__ == "__main__":
    main()