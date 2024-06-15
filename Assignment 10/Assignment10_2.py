

import os
import sys

def RenameFile(foldername,oldextension,newextension):
    if(os.path.isabs(foldername) == False):
        foldername = os.path.abspath(foldername)

    for foldname,_,filename in os.walk(foldername):
        for name in filename:
            fname,extension = os.path.splitext(os.path.join(foldname,name))
            print(extension.lower(), oldextension.lower())
            if(extension.lower() == oldextension.lower()):
                os.replace(fname+extension, os.path.join(foldname,fname)+newextension)

def main():
    if(len(sys.argv) == 4):
        try:
            RenameFile(sys.argv[1],sys.argv[2],sys.argv[3])
        except Exception as ex:
            print(ex)

if __name__ == "__main__":
    main()