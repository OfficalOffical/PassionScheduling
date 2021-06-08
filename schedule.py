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
    highPriority(x,y,(temp*0.5),100)#SJF








def highPriority(x, y, ratio, averageTime):#SJF
    global idleTime #May i put waiting time to other scheduling algo's
    idleTime=0
    tempX = x
    tempY = y
    temp = 0
    for i in range(int(ratio)):
        temp = req.findShortest(tempX,tempY)
        if (temp != -1):
            print(tempY[temp])
            tempY[temp] -=1
        else:
            idleTime += 1
    print(":", idleTime)
    print(tempX,tempY)
    return tempY


