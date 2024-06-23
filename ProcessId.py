import psutil
import smtplib

def DisplayProcess():
    print("List of running processess are : ")

    print("-----------------------------------")

    for proc in psutil.process_iter(['pid','name','username']):
        print(proc.info)

    print("-----------------------------------------")


def CreateLog(FileName = "Log.log"):
    fd = open(FileName,"w")

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

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("mayurdimble99@gmail.com", "*****")
    message = "Message_you_need_to_send"
    s.sendmail("mayurdimble99@gmail.com", "mayurdimble412105@gmail.com", message)
    s.quit()

def main():
    #DisplayProcess()
    CreateLog()

if __name__ == "__main__":
    main()