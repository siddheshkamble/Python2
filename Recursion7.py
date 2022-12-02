
def Display(No):
    iSum = 0  
    while(No > 0):
        iSum = iSum + No
        No = No -1
    return iSum

def main():

    Num = int(input("Enter the number : "))
    Ret = Display(Num)
    print("Addition is :", Ret)
if __name__=="__main__":
    main()