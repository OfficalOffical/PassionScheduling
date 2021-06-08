import req







#Turnaround time = Exit time - Arrival time
#Turnaround time = Burst time + Waiting time
#Waiting time = Turnaround time - Burst time
#Througput = waiting time /3


class process:
    def __init__(self,ID, start, end,):
        self.ID = ID
        self.start = start
        self.end = end


def MLFQ(x,y):
    print(x)
    print(y)
    temp = req.reqTime(y)
    global P1,P2,P3
    P1 = process(0, -1, -1)
    P2 = process(1, -1, -1)
    P3 = process(2, -1, -1)

    highPriority(x,y,(temp*0.5))#SJF
    print(P1.start)







def highPriority(x, y, ratio):#SJF
    global idleTime #May i put waiting time to other scheduling algo's
    idleTime=0
    tempX = x
    tempY = y
    temp = 0
    for i in range(int(ratio)):
        temp = req.findShortest(tempX,tempY)
        if (temp != -1):
            print(i," : ",tempY[temp])
            print(temp)
            tempY[temp] -=1
        else:
            idleTime += 1
    print(":", idleTime)
    print(tempX,tempY)
    return tempY

def checkStartEnd(time,ID):
    if(ID == 0):



