
def Fact(No):
    if(No <= 0):
        return 1
    else:
        return(No * Fact(No - 1))

def main():

    Num = int(input("Enter the number : "))
    Ret = Fact(Num)
    print("Factorial is :", Ret)
if __name__=="__main__":
    main()