#this program show error
def Display(No):
    iCnt = 0

    if(iCnt<No):
        print("Hello")
        iCnt = iCnt + 1
        Display(No)     #recursion call 

Display(4)
