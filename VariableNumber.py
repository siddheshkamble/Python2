# def Add(*Values):
#     # print(type(Values))
#     # print("Number of arguments are :", len(Values))
#     Sum = 0
#     for no in Values:
#         Sum = Sum + no

#     return Sum

def Add(*Values):
    Sum = 0
    for i in range(0,len(Values)):
        Sum = Sum + Values[i]

    return Sum

def main():
    Ans = 0
    Ans = Add(1,7,9,4,6,5)
    print("Addition is :",Ans)

if __name__=="__main__":
    main()