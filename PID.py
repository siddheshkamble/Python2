import os

def main():
    print("PID of current process is:", os.getpid())
    print("PPID of parent process is:", os.getppid())

if __name__=="__main__":
    main()
