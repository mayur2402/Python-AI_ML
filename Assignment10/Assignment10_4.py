import os
import shutil
import sys

def CopyDirectory(ExistingDir,NewDir,newextesion):
    if(os.path.isabs(ExistingDir)):
        ExistingDir = os.path.abspath(ExistingDir)

    if (os.path.exists(NewDir) == False):
        os.makedirs(NewDir)
    
    for foldername,subfoldername,filename in os.walk(ExistingDir):

        for name in filename:
            fname,extension = os.path.splitext(os.path.join(foldername,name))
            if(extension.lower() == newextesion.lower()):
                shutil.copy(os.path.join(foldername,name), os.path.join(NewDir,name))

def main():

    try:
        CopyDirectory(sys.argv[1],sys.argv[2],sys.argv[3])
    except Exception as ex:
        print(ex)   


if __name__ == "__main__":
    main()