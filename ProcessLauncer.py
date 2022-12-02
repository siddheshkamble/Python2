import os
from sys import *
import schedule
import time
import datetime
from subprocess import Popen, PIPE

def ProcessLauncher(FileName):
    process = Popen(['swfdump', '/tmp/filename.swf', '-d'], stdout=PIPE, stderr=PIPE),stdout, stderr = process.communicate()

def main():
    print("Process Launcher application")

    if(len(argv) < 2):
        print("Insufficient Argument")
        exit()

    if(argv[1] == "-h"):
        print("This script will open file")
        exit()

    if(argv[1] == "-u"):
        print("Usage : Application_name File_Name")
        exit()
    try:
        print("Siddhesh")
        print("Current time is : ", datetime.datetime.now())

        schedule.every(1).minutes.do(ProcessLauncher(argv[1]))

    except Exception:
        while(True):       
            schedule.run_pending()
            time.sleep(1) 

    except ValueError:
        print("Error : Invalid datatypes of input")
    
    except Exception:
        print("Error : Invalid Input")

if __name__ =="__main__":
    main()