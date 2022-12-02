
def Display(No):
    if(No > 0):
        print("Hello")
        No = No - 1
        Display(No)     #recursive call

Display(4)      #function call
