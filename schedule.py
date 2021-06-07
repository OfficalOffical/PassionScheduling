import req


def MLFQ(x,y):
    print(x)
    print(y)
    yemp = req.reqTime(y)

    highPriority(x,y,(yemp*0.5))#SJF







def highPriority(x,y,ratio):#SJF
    tempX = x
    tempY = y
    temp = 0
    for i in range(int(ratio)):
       temp = req.findShortest(tempX,tempY)
       if (temp != -1):
           tempY[temp] -=1

    print(tempX,tempY)
