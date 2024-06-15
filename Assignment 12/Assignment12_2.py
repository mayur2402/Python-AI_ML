

import sys
import psutil


def RunningProcess(processName):
    dictProcess = {}
    iCnt = 0
    for process in psutil.process_iter(["pid","name","username"]):
       dictProcess[iCnt] = process.info
       iCnt += 1

    for data in dictProcess:
        if(dictProcess[data]['name'] == processName):
            print(dictProcess[data])

def main():
    if(len(sys.argv) != 2):
        print("Invalid Argument")
        exit()

    print("Running Process")
    RunningProcess(sys.argv[1])

if __name__ == "__main__":
    main()