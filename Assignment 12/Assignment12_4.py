

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import smtplib
import sys
import psutil

def SendMail(folderName):
    try:
        fromMail = "mayurmailtest@gmail.com"
        toMail = "mayurdimble99@gmail.com"

        message = MIMEMultipart()
        message["From"] = fromMail
        message["to"] = toMail

        body = "Running Processess"

        Subject = "Running Processess"

        message["Subject"] = Subject

        message.attach(MIMEText(body,"plain"))

        attachement = open(folderName,"rb")

        p = MIMEBase("application","octet-stream")
        p.set_payload((attachement).read())

        encoders.encode_base64(p)

        p.add_header("Content-Disposition", folderName)

        message.attach(p)


        s = smtplib.SMTP("smtp.gmail.com",587)
        s.starttls()
        s.login(fromMail,"___ ___ ___ ___")

        text = message.as_string()
        s.sendmail(fromMail,toMail,text)

        s.quit()


    except Exception as ex:
        print(ex)

def GetRunningProcess(FolderName):
    dictProcess = {}
    iCnt = 0
    for process in psutil.process_iter(["pid","name","username"]):
       dictProcess[iCnt] = process.info
       iCnt += 1

    if(os.path.isdir(FolderName) == False):
        FolderName = os.makedirs(FolderName)
    print(FolderName)
    if(os.path.isabs(FolderName) == False):
        FolderName = os.path.abspath(FolderName)

    fileName = "log.txt"

    FolderName = os.path.join(FolderName,fileName)

    f = open(FolderName,"w")
    f.write("PID\t\tNAME\t\tUSERNAME\n" )
    for data in dictProcess:
        f.write( str(dictProcess[data]["pid"]) +"\t")
        f.write("\t" +dictProcess[data]["name"] +"\t")
        f.write("\t" +str(dictProcess[data]["username"]) +"\n")

    f.close()
    return FolderName

def main():

    if(len(sys.argv) != 2 ):
        print("Enter Valid Command Line Argument")

    FolderName = GetRunningProcess(sys.argv[1])
    print(FolderName)

    SendMail(FolderName)

if __name__ == "__main__":
    main()