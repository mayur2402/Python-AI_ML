import os
import time
import psutil
import smtplib
import schedule

def DisplayProcess():
    print("List of running processess are : ")

    print("-----------------------------------")

    for proc in psutil.process_iter(['pid','name','username']):
        print(proc.info)

    print("-----------------------------------------")


def CreateLog(DirName = "Log",FileName = "Log.log"):

    if(os.path.isdir(DirName) == False):
        DirName = os.makedirs(DirName)

    name = os.path.join(DirName,"Log%s.log" %time.ctime())
    name = name.replace(" ","")
    name = name.replace(":","_")
    fd = open(name,"w")

    separator = "-"*70

    fd.write(separator + "\n")
    fd.write("Mayur Process Log" + "\n")
    fd.write(separator + "\n")
    fd.write("Content of log file")
    datadict = {}
    icnt = 0
    for proc in psutil.process_iter(['pid','name','username']):
        datadict[icnt] = proc.info
        icnt = icnt + 1
    jcnt = 0
    for data in datadict:
        fd.write(str(datadict[data]) + "\n")
        jcnt = jcnt + 1

    fd.write(separator + "\n")

    fd.close()

def main():
    #DisplayProcess()
    schedule.every(1).minutes.do(CreateLog)    

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()