import datetime
import schedule

def Schedule_Minutes():
    print("Scheduler execute after each minute : ",datetime.datetime.now())

def main():
    print("Current Time is : ",datetime.datetime.now())
    
    schedule.every(1).minutes.do(Schedule_Minutes)

if __name__ == "__main__":
    main()