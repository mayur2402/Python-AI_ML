

import psutil


def RunningProcess():

    for process in psutil.process_iter(["pid","name","username"]):
       print(process.info)

def main():
    print("Running Process")
    RunningProcess()

if __name__ == "__main__":
    main()