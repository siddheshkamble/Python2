
def Add(No):
    if(No <= 0):
        return 0
    else:
        return(No + Add(No - 1))

def main():

    Num = int(input("Enter the number : "))
    Ret = Add(Num)
    print("Addition is :", Ret)
if __name__=="__main__":
    main()