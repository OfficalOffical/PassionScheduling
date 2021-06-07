import req


def MLFQ(x,y):
    print(x)
    print(y)
    temp = req.reqTime(y)


    highPriority(x,y,(temp*0.5),aT)#SJF
    print(aT)







def highPriority(x,y,ratio,averageTime):#SJF
    tempX = x
    tempY = y
    temp = 0
    for i in range(int(ratio)):
        temp = req.findShortest(tempX,tempY)
        if (temp != -1):
            print(tempY[temp])
            tempY[temp] -=1
        else:
            print("GAYYYYY")


    print(tempX,tempY)
