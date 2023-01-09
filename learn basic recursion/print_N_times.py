def printNos(N):
    #Your code here
    if N <= 0:
        return 
    else:
        printNos(N-1)
        print(N,end = " ")

printNos(15)
