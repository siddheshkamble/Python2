#back tracking
#head recursion
def Display(No):
    if(No > 0):
        No = No - 1
        Display(No)
        print(No)

def main():

    Num = int(input("Enter the number"))
    Display(Num)

if __name__=="__main__":
    main()
    

