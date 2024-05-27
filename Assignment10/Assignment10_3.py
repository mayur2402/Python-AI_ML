import os
import shutil
import sys

def CopyDirectory(ExistingDir,NewDir):
    if(os.path.isabs(ExistingDir)):
        ExistingDir = os.path.abspath(ExistingDir)
    print(os.path.exists(NewDir))
    if (os.path.exists(NewDir) == False):
        os.makedirs(NewDir)
    
    for foldername,subfoldername,filename in os.walk(ExistingDir):

        for name in filename:
            shutil.copy(os.path.join(foldername,name), os.path.join(NewDir,name))

def main():

    try:
        CopyDirectory(sys.argv[1],sys.argv[2])
    except Exception as ex:
        print(ex)   


if __name__ == "__main__":
    main()