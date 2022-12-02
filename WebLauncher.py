import os
import webbrowser
from sys import *
import readline
with urllib.request import urlopen

def is_connencted():
    try:
        urlopen('https://www.google.com/')
        return True
    except Exception as err:
        return False

def Find(string):
    url = re.findall("http[s*]:[a-zA-Z0-9_.+-/#~]+ ", string)
    return url

def WebLauncher(path):
    with open(path) as fp:
        for line in fp:
            url = Find(line)
            for str in url:
                webbrowser.open(str, new = 2)

def main():

    print("----Siddhesh Kamble----")

    print("Application name :", argv[0])

    if(len(argv) != 2):
        print("Invalid number of arguments")
        exit()

    if((argv[1]=="-h") or (argv[1]=="-H")):
        print("The script is used to open Url's in file")
        exit()

    if((argv[1]=="-u") or (argv[1]=="-U")):
        print("Usage : ApplicationName FileName")
        exit()

    try:
        connected = is_connencted()

        if connected:
            WebLauncher(argv[1])
        else:
            print("Unable to connect to internet...")

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception as E:
        print("Error : Invaild Inputs", E)


if __name__ == "__main__":
    main()