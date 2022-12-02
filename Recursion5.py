#tail recursion
def Display(No):
    if(No > 0):
        print(No)
        No = No - 1
        Display(No)

def main():

    Num = int(input("Enter the number"))
    Display(Num)

if __name__=="__main__":
    main()