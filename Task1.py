import schedule
import time
import datetime

def Fun():
    print("Inside Fun")     #logic

def main():
    print("Inside task schedular")

    schedule.every(1).minutes.do(Fun)

    while(True):        #unconditional infinte loop
        schedule.run_pending()
        time.sleep(1)       #1 is in second

if __name__ == "__main__":
    main()

# step 1: sudo apt update
# step 2: sudo apt install python3-pip
# step 3: pip3 --version