import datetime
import time
import schedule

def Schedule_Minutes():
    print("Scheduler execute after each minute : ",datetime.datetime.now())

def Schedule_Hour():
    print("Scheduler execute after each hour : ",datetime.datetime.now())

def Schedule_Sunday():
    print("Scheduler execute after each sunday : ",datetime.datetime.now())


def main():
    print("Current Time is : ",datetime.datetime.now())
    
    schedule.every(1).minutes.do(Schedule_Minutes)
    schedule.every(1).hour.do(Schedule_Hour)
    schedule.every(1).sunday.do(Schedule_Sunday)

    while True:
        schedule.run_pending()
        time.sleep(1)
if __name__ == "__main__":
    main()