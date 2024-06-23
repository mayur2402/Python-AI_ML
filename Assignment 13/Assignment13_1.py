from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import hashlib
import smtplib
from sys import argv
import os
import time

def CalculateFileHash(fileName,blockSize = 1024):

    binaryFile = open(fileName,"rb")
    hasher = hashlib.md5()

    buffer = binaryFile.read(blockSize)

    while len(buffer) > 0:
        hasher.update(buffer)
        buffer = binaryFile.read(blockSize)

    binaryFile.close()
    return hasher.hexdigest()


def GetDuplicateFiles(dirName):
    if os.path.isabs(dirName) == False:
        dirName = os.path.abspath(dirName)

    if os.path.isdir(dirName) == False:
        print("Invalid Directory")
        exit()
    
    fileDict = {}
    for foldername,subfoldername,filename in os.walk(dirName):

        for fname in filename:
            path = os.path.join(foldername,fname)

            fileHash = CalculateFileHash(path)
            
            if fileHash in fileDict:
                print(path)
                fileDict[fileHash].append(path)
            else:
                fileDict[fileHash] = [path]

    return fileDict

def DeleteDuplicateFile(DictFile,filename):
    filename = open(filename,"w")
    duplicate = list(filter(lambda x : len(x) > 1,DictFile.values()))
    if(len(duplicate) > 0):
        icnt = 0
        for data in duplicate:
            for ddate in data:
                icnt = icnt + 1
                if icnt >= 2:
                    try:
                        filename.write(ddate + "\n")
                        os.remove(ddate)
                    except AttributeError as ex:
                        filename.write(ex)
                    
            icnt = 0

def SendMail(tomail,folderName):
    try:
        fromMail = "mayurmailtest@gmail.com"
        toMail = tomail

        message = MIMEMultipart()
        message["From"] = fromMail
        message["to"] = toMail

        body = "Duplicate Files"

        Subject = "Duplicate Files"

        message["Subject"] = Subject

        message.attach(MIMEText(body,"plain"))

        attachement = open(folderName,"rb")
        print(attachement)
        p = MIMEBase("application","octet-stream")
        p.set_payload((attachement).read())

        encoders.encode_base64(p)

        p.add_header("Content-Disposition", folderName)

        message.attach(p)


        s = smtplib.SMTP("smtp.gmail.com",587)
        s.starttls()
        s.login(fromMail,"_____")

        text = message.as_string()
        s.sendmail(fromMail,toMail,text)

        s.quit()


    except Exception as ex:
        print(ex)

def main():
    print("-------Duplicate File Removal--------")
    print("Application Name is " + argv[0])
    FileName = "Log/log_" + time.ctime().replace(" ","_").replace(":","_") + ".txt"
    if(os.path.isdir("Log") == False):
        os.mkdir("Log")
    #FileName = os.path.abspath(FileName)
    f = open(FileName,'w')
    f.write("-------Duplicate File Removal--------\n")
    if(len(argv) != 3):
        print("Invalid Command Line Argument")
        exit()

    if(argv[1] == "-h" or argv[1] == "-H"):
        print("This Script is used to delete duplicate files")
        exit()

    if(argv[1] == "-u" or argv[1] == "-U"):
        print("Usage : ApplicationName AbsolutePath")
        exit()
    try:
        checkSum = {}
        checkSum = GetDuplicateFiles(argv[1])
        DeleteDuplicateFile(checkSum,FileName)
        SendMail(argv[2],FileName)
    except Exception as ex:
        f.write(ex)

if __name__ == "__main__":
    main()